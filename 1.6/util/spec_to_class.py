import argparse
import pathlib
import os
import re

from typing import List, Dict

TAB = "    "

"""
## default
- .py 파일의 내용이 비워져 있을 경우 로그로 출력

## message
- [name] [type] [card] [desc] 형식으로 나뉨
    - [name] : 카멜케이스 형식의 이름
    - [type] 의 종류는 다음과 같음
        - 기본 타입 : "Text Length undefined(string)", "anyURI(url format string)", "integer", "dateTime", "integer [name] >= 0" 과 같은 형태 
        - 정의 타입 : 첫 문자가 대문자로 시작하는 파스칼 케이스 형식
    - [card]
        - 1..1 : required - 1개
        - 0..1 : optional - 0개 또는 1개
        - 0..* : optional - 리스트 형식의 0개 이상
        - 1..* : required - 리스트 형식의 1개 이상
    - [desc]
        - "Required" 또는 "Optional" 으로 시작

## type
- [name] [type] [card] [desc] 형식으로 나뉨
    - message 형식이랑 동일

- [name] [desc] 형식으로 나뉨 -> enum 타입
    - [name] : 대문자로 시작하는 이름 (문자열 형식)
    - [desc] : enum 타입 설명
"""

def get_empty_class_content(class_name: str) -> str:
    class_header = f"""class {class_name}:"""
    init_content = """
    def __init__(self):
        pass
    """
    value_content = """
    def get_value(self):
        result = {}
        return result
    """
    sample_content = """
    @classmethod
    def get_sample(cls, option=False):
        result = {}
        return result
    """

    result = []
    result.append(class_header)
    result.append(init_content)
    result.append(value_content)
    result.append(sample_content)

    return "".join(result)

def get_enum_class_content(class_name: str, metadata: List) -> str:
    import_header = """from enum import Enum
    """

    class_header = f"""class {class_name}(Enum):"""

    docstring = """
    \"\"\"
    EnumType class"""
    body = ""

    for data in metadata:
        docstring += f"""
    : {data['name']} : {data['desc']}"""
        body += f"""
    {data['name'].upper()} = \"{data['name']}\""""
        
    docstring += """
    \"\"\""""
    body += """\n
    def get_value(self):
        return self.value\n
    @classmethod
    def get_members(cls):
        return [m for m in cls]\n
    @classmethod
    def get_sample(cls, option=False):
        value = __import__('random').choice(list(cls))
        return value.value
    """

    return "\n".join([import_header, class_header, docstring, body])

def get_str_class_content(class_name, metadata: List) -> str:
    class_header = f"""class {class_name}(str):"""
    body = f"""
    MAX_LENGTH = {metadata[0]['max_length']}

    def __new__(cls, value):
        if not isinstance(value, str):
            raise TypeError("LimitedStr only accepts string values.")

        if len(value) > cls.MAX_LENGTH:
            raise ValueError(f"String exceeds maximum length of {{cls.MAX_LENGTH}} characters.")

        return super().__new__(cls, value)

    @classmethod
    def get_sample(cls, option=False):
        min_len = 1
        max_len = cls.MAX_LENGTH
        random = __import__("random")
        string = __import__("string")

        length = random.randint(min_len, max_len)
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length))
    """

    return "\n".join([class_header, body])
    
def get_class_content(class_name: str, metadata: List) -> str:
    """
    example metadata
    [
        {'name': 'connectorId', 
        'type': 'integer connectorId >= 0', 
        'card': '1..1', 
        'desc': "Required. The id of the connector for which availability needs to change. Id '0' (zero) is used if the availability of the Charge Point and all its connectors needs to change."
        }, 
        {'name': 'type', 
        'type': 'AvailabilityType', 
        'card': '1..*', 
        'desc': 'Required. This contains the type of availability change that the Charge Point should perform.'
        },
        {'name': 'data', 
        'type': 'dateTime', 
        'card': '1..1', 
        'desc': 'Required. This contains the type of availability change that the Charge Point should perform.'
        },
        {'name': 'test', 
        'type': 'integer connectorId >= 0', 
        'card': '0..*', 
        'desc': "Optional. The id of the connector for which availability needs to change. Id '0' (zero) is used if the availability of the Charge Point and all its connectors needs to change."
        }
    ]
    """
    class_header = f"class {class_name}:"

    try:
        import_header = get_file_header_content(metadata)
        init_content = get_class_init_content(metadata)
        value_func_content = get_class_value_func_content(metadata)
        sample_func_content = get_class_sample_func_content(metadata)
    except ValueError as e:
        print(f"'{filename}' {e}")

    result = []
    result.append(import_header)
    result.append(class_header)
    result.append(init_content)
    result.append(value_func_content)
    result.append(sample_func_content)

    return "\n".join(result)

def get_file_header_content(metadata: List) -> str:
    known_type = {"Text": "str", "anyURI":"str", "integer":"int", "dateTime":"datetime", "decimal": "float", "boolean": "bool", "String": "str"}
    import_header_set = set()
    typing_header = ""

    use_datetime = False
    use_typing_list = False
    use_typing_optional = False

    for data in metadata:
        type_name = data['type']
        card = data['card']
        desc = data['desc']

        # check datetime
        type_info = known_type.get(type_name.split(" ")[0])
        if not type_info:
            import_header_set.add(type_name)
        elif type_info == "datetime":
            use_datetime |= True
        
        # check typing List
        if "*" in card:
            use_typing_list |= True
        
        # check typing Optional
        if desc.startswith("Optional"):
            use_typing_optional |= True

    result = []
    if use_datetime:
        result.append("from datetime import datetime\n")
    
    if use_typing_list:
        typing_header += "from typing import List"
    
    if use_typing_optional:
        typing_header += ", Optional" if typing_header else "from typing import Optional"
    
    if typing_header:
        result.append(typing_header + '\n')

    if import_header_set:
        import_header = "\n".join([f"from type.{name} import {name}" for name in import_header_set ]) + '\n'
        result.append(import_header)

    return "\n".join(result)
    
def get_class_init_content(metadata: List) -> str:
    known_type = {"Text": "str", "anyURI":"str", "integer":"int", "dateTime":"datetime", "decimal": "float", "boolean": "bool", "String": "str"}
    init_header = """
    def __init__(self"""

    require_argv = ""
    optional_argv = ""

    required_init_body = ""
    optional_init_body = ""

    for data in metadata:
        name = data['name']
        type_name = data['type']
        card = data['card']
        desc = data['desc']

        # check known type
        type_info = known_type.get(type_name.split(" ")[0])
        if not type_info:
            type_info = type_name

        # check list type
        type_info = f"List[{type_info}]" if "*" in card else type_info

        if desc.startswith("Required"):
            required_init_body += f"""
        self.{name} = {name}"""
            require_argv += f", {name}: {type_info}"
        elif desc.startswith("Optional"):
            optional_init_body += f"""
        if {name}:
            self.{name} = {name}"""
            type_info = f"Optional[{type_info}]"
            optional_argv += f", {name}: {type_info}= None"
        else:
            raise ValueError(f"'{name}' : There is unmatched desc value")
        
    init_header += require_argv
    if optional_argv:
        init_header += optional_argv
    
    if len(init_header) > 180:
        tokens = init_header.split(", ")
        init_header = f",\n{TAB*2}".join(tokens)
        init_header += f"\n{TAB}):"
    else:
        init_header += "):"

    return "".join([init_header, required_init_body, optional_init_body])

def get_class_value_func_content(metadata: List) -> str:
    known_type = {"Text": "str", "anyURI":"str", "integer":"int", "dateTime":"datetime", "decimal": "float", "boolean": "bool", "String": "str"}
    func_header = """
    def get_value(self):"""
    func_footer = """
        return result"""

    required_func_body = """
        result = {"""
    optional_func_body = ""

    for data in metadata:
        name = data['name']
        type_name = data['type']
        card = data['card']
        desc = data['desc']

        value = name

        # check occp type
        type_info = known_type.get(type_name.split(" ")[0])
        if not type_info:
            value += ".get_value()"
        
        # check datetime type
        if type_info == "datetime":
            value += ".isoformat().split('.')[0] + 'Z'"

        # check list type
        if "*" in card:
            value = f"[ {value} for {name} in self.{name} ]"
        else:
            value = f"self.{value}"

        if desc.startswith("Required"):
            required_func_body += f"""
            \"{name}\" : {value},"""
        elif desc.startswith("Optional"):
            optional_func_body += f"""
        if self.{name}:
            result['{name}'] = {value}"""

    required_func_body += """
        }"""

    result = []
    result.append(func_header)
    result.append(required_func_body)
    if optional_func_body:
        result.append(optional_func_body)
    result.append(func_footer)

    return "".join(result)

def get_class_sample_func_content(metadata: List) -> str:
    """
    json에 맞는 샘플 데이터를 생성
    나중에 여기에 mutate 기능 추가할 예정
    """
    func_header = """
    @classmethod
    def get_sample(cls, option=False):"""
    func_footer = """
        return result"""
    
    required_func_body = """
        result = {}"""
    optional_func_body = ""

    for data in metadata:
        name = data['name']
        type_name = data['type']
        card = data['card']
        desc = data['desc']

        value = ''

        type_info = type_name.split(" ")[0]
        if type_info == "Text" or type_info == "String":
            value = "\"string\""
        elif type_info == "decimal":
            value = "1.0"
        elif type_info == "boolean":
            value = "__import__('random').choice([True, False])"
        elif type_info == "anyURI":
            value = "\"http://example.com/\""
        elif type_info == "integer":
            value = "1"
        elif type_info == "dateTime":
            value = "datetime.now().isoformat().split('.')[0] + 'Z'"
        else:
            value = f"{type_name}.get_sample(option=option)"

        if "*" in card:
            value = f"[ {value}, ]"
        
        if desc.startswith("Required"):
            required_func_body += f"""
        result['{name}'] = {value}"""
        elif desc.startswith("Optional"):
            optional_func_body += f"""
        if option:
            result['{name}'] = {value}"""
    
    result = []
    result.append(func_header)
    result.append(required_func_body)
    if optional_func_body:
        result.append(optional_func_body)
    result.append(func_footer)

    return "".join(result)

def get_enum_metadata(file: str) -> List:
    """
    str 형식의 파일 내용을 파싱하여 [name], [desc] 등의 메타데이터 형식의 데이터를 반환
    :param file: 파일의 내용
        "Accepted Identifier is allowed for charging."
    :return:
        [
            {
                "name": "Accepted",
                "desc": "Required. This contains ... "
            },
            ...
        ]
    """

    pattern = re.compile(r'^(\w+)\s+(.*)$', re.MULTILINE)
    result = [{"name":name, "desc":desc.strip()} for name, desc in pattern.findall(file)]
    
    return result

def get_str_metadata(file: str) -> List:
    """
    str 형식의 파일 내용을 파싱하여 [name], [max_length] 등의 메타데이터 형식의 데이터를 반환
    :param file: 파일의 내용
        "CiString[25] String is case insensitive."
    :return:
        [
            {
                "max_length": 25
            }    
        ]
    """
    line = file.strip()
    token = line.strip().split()[0]
    
    len_sidx = token.find("[")
    len_eidx = token.find("]")
    max_length = int(token[len_sidx+1:len_eidx])

    result = [{"max_length":max_length}]
    return result


def get_object_metadata(file: str) -> List:
    """
    str 형식의 파일 내용을 파싱하여 [name], [type], [card], [desc] 등의 메타데이터 형식의 데이터를 반환
    :param file: 파일의 내용
        "idTagInfo IdTagInfo 1..1 Required. This contains ... "
    :return:
        [
            {
                "name": "idTagInfo",
                "type": "IdTagInfo",
                "card": "1..1"
                "desc": "Required. This contains ... "
            },
            ...
        ]
    """
    result = []

    for line in file.strip().split("\n"):
        tokens = line.strip().split()

        name = tokens[0]

        card_idx = next(i for i, token in enumerate(tokens) if re.match(r'\d+\.\..', token))
        card = tokens[card_idx]

        type_str = ' '.join(tokens[1:card_idx])

        desc = ' '.join(tokens[card_idx+1:])

        result.append({
            "name": name,
            "type": type_str,
            "card": card,
            "desc": desc
        })

    return result

def is_object(file: str) -> bool:
    """
    파일의 첫 문자가 대문자인지 소문자인지 확인하여 object 형식인지 enum 형식인지 구분합니다.
    :param file: 파일의 내용
        object example : "idTagInfo IdTagInfo 1..1 Required. This contains ... "
        enum example   : "Accepted Identifier is allowed for charging."
    :return:
        False or True
    """
    if file[0].islower():
        return True
    return False

def is_str(file: str) -> bool:
    """
    enum 타입 형식의 파일 내용에서 CiString 타입인지, 아님 enum 타입인지를 구분합니다.
    :param file: 파일의 내용
        str type example : "CiString[20] String is case insensitive."
        enum example : "Accepted Identifier is allowed for charging."
    :return:
        False or True
    """
    if "CiString[" in file:
        return True
    return False

def get_class_name(filename:str) -> str:
    tokens = filename.split(".")
    action_name = tokens[0]
    if len(tokens) >= 3:
        class_name = f"{action_name}Request" if filename.split(".")[1] == "req" else f"{action_name}Response"
    else:
        class_name = action_name

    return class_name


def handle_convert_message_file(args):
    input_dir = pathlib.Path(args.i)
    output_dir = pathlib.Path(args.o)
    cnt = 0

    if not output_dir.exists():
        output_dir.mkdir()
    
    for file in input_dir.iterdir():
        file_name = file.name
        file_data = file.open("r").read()
        print(f"[+] Working on '{file_name}'.")
        class_name = get_class_name(file_name)

        if not file_data:
            print(f"[-] '{file_name}' is empty.")
            result = get_empty_class_content(class_name)
        else:
            if is_object(file_data):
                metadata = get_object_metadata(file_data)
                result = get_class_content(class_name, metadata)
            else:
                raise ValueError(f"'{file_name}' : This is not object spec file.")

        file_path = output_dir / (class_name + ".py")
        try:
            file_path.open("w").write(result)
            cnt += 1
        except Exception as e:
            print(e)
    
    return cnt

def handle_convert_type_file(args):
    input_dir = pathlib.Path(args.i)
    output_dir = pathlib.Path(args.o)
    cnt = 0

    if not output_dir.exists():
        output_dir.mkdir()

    for file in input_dir.iterdir():
        file_name = file.name
        file_data = file.open("r").read()
        print(f"[+] Working on '{file_name}'.")
        class_name = get_class_name(file_name)

        if not file_data:
            print(f"[-] '{file_name}' is empty.")
            continue # 기능 구현하기
        else:
            if not is_object(file_data):
                if is_str(file_data):
                    metadata = get_str_metadata(file_data)
                    result = get_str_class_content(class_name, metadata)
                else:
                    metadata = get_enum_metadata(file_data)
                    result = get_enum_class_content(class_name, metadata)
                    #result = get_empty_class_content(class_name)
            else:
                metadata = get_object_metadata(file_data)
                result = get_class_content(class_name, metadata)
        
        file_path = output_dir / (class_name + ".py")
        try:
            file_path.open("w").write(result)
            cnt += 1
        except Exception as e:
            print(e)
    
    return cnt


def main():
    parser = argparse.ArgumentParser(description="convert type/message spec to class or enum python file")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for cmd in ["message", "type"]:
        sub = subparsers.add_parser(cmd, help=f"{cmd.capitalize()}")
        sub.add_argument("-i", required=True, help="Input directory path")
        sub.add_argument("-o", required=True, help="Output directory path")

    args = parser.parse_args()

    if args.command == "message":
        print("[+] Start creating message file.")
        cnt = handle_convert_message_file(args)
        print(f"[-] Total {cnt} files finish..")
    elif args.command == "type":
        print("[+] Start creating type file.")
        cnt = handle_convert_type_file(args)
        print(f"[-] Total {cnt} files finish..")

if __name__ == "__main__":
    main()
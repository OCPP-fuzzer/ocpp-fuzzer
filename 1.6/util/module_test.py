import pathlib

from typing import List

TAB = " "*4

def get_files(dir_path: str) -> List[pathlib.Path]:
    file_path = pathlib.Path(dir_path)
    if not file_path.exists():
        print("Directory not exists.")
        exit(-1)
    
    return [ x for x in file_path.iterdir() if x.is_file() ]

def write_module_file(module_path: str, import_file_list: List, option="a"):
    content = ""
    module_file = pathlib.Path(module_path)
    
    for file in import_file_list:
        parent = file.parent.name
        module = file.name.split(".")[0]
        content += f"from {parent}.{module} import {module}\n"

    try:
        module_file.open(option).write(content)
    except Exception as e:
        print(e)

def create_init_file(init_path: str, import_file_list: List, option="w"):
    content = ""
    footer = "__all__ = ["
    init_file = pathlib.Path(init_path)

    for file in import_file_list:
        module = file.name.split(".")[0]
        content += f"from {module} import {module}\n"
        footer += f"\"{module}\", "

    if len(footer) > 180:
        tokens = footer.split(", ")
        footer = f",\n{TAB}".join(tokens)
    
    footer += "]"
    result = "\n".join([content, footer])

    try:
        init_file.open(option).write(result)
    except Exception as e:
        print(e)

def main():
    message_files = get_files("../message")
    module_file = "../module.py"
    write_module_file(module_file, message_files)
    # init_file = "../message/__init__.py"
    # create_init_file(init_file, message_files)

    # type_files = get_files("../type")
    # init_file = "../type/__init__.py"
    # create_init_file(init_file, type_files)


if __name__ == "__main__":
    main()
import os
import pathlib

from typing import List

def get_requests(dir_path: str) -> List:
    file_path = pathlib.Path(dir_path)
    if not file_path.exists():
        print("Directory not exists.")
        exit(-1)
    
    return [ x.name.split(".")[0] for x in file_path.iterdir() if x.is_file() ]

def cmd_decorator(cmd, desc):
    boundary_len = 60 - len(desc)
    boundary = "=" * (boundary_len // 2)

    print(f"{boundary} {desc} {boundary}")
    os.system(cmd)
    print("\n\n")

def main():
    message_path = "../message"
    requests_list = get_requests(message_path)
    cnt = 0
    
    for request in requests_list:
        cmd = f"python3 ../run.py --request={request} --url=http://test.test --option=True"
        cmd_decorator(cmd, request)
        cnt += 1

    print(f"Total requests : '{cnt}'")

if __name__ == "__main__":
    main()

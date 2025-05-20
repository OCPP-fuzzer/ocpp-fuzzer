import argparse
import pathlib
import os

def handle_create_file(args):
    cnt = 0
    list_file_path = pathlib.Path(args.i)
    output_path = pathlib.Path(args.o)
    print(f"[+] input file : {list_file_path}")
    print(f"[+] output dir : {output_path}")

    if not list_file_path.exists():
        print("[-] There is no input file")
        exit(-1)

    if not output_path.exists():
        print("[-] There is not output directory")
        exit(-1)
    
    data = list_file_path.open("r").read()
    data = data.split(". ")
    data = [ x for x in data if x]

    file_path_list = [ output_path / (data[i].strip() + ".py") for i in range(1, len(data), 2)]

    for file in file_path_list:
        try:
            file.open("w")
            cnt+=1
        except:
            print(f"Error - {file.as_posix()}")

    print(f"[-] {cnt} file complete")

def main():
    parser = argparse.ArgumentParser(description="Preloader")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for cmd in ["create"]:
        sub = subparsers.add_parser(cmd, help=f"{cmd.capitalize()}")
        sub.add_argument("-i", required=True, help="Input file path")
        sub.add_argument("-o", required=True, help="Output directory path")

    args = parser.parse_args()

    if args.command == "create":
        handle_create_file(args)

if __name__ == "__main__":
    main()
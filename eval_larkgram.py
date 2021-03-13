#!/usr/bin/python3
import sys
from lark import Lark
from tqdm import tqdm

verbose = True

def main():
    sys.setrecursionlimit(10000)
    if len(sys.argv) < 3:
        print("Usage: {sys.argv[0]} <grammar-file> <input-files>")
        exit(1)

    grammar = r"".join(open(sys.argv[1]).readlines())
    if verbose: print("creating parser...")
    parser = Lark(grammar)
    if verbose: print("parser created.")
    count = 0
    success = 0
    for in_file in tqdm(sys.argv[2:]):
        count += 1
        try:
            v = parser.parse(open(in_file).read().rstrip())
            if verbose:
                print("Succesfully parsed: ", in_file)
            success += 1
        except Exception as e:
            print("Failed to parse: ", in_file)
            print("Because:", e)
        if verbose: print(f"\nparsed {success} of {count}\n")
    if verbose:
        print("-----------------------------")
    print(f"Succesfully parsed {100*success/count}% of infiles.")
    print(f"Recall: {success/count}")

if __name__ == '__main__':
    main()

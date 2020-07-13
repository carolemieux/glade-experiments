#!/usr/bin/python3
import sys
from lark import Lark

grammar ="""start: c
c: "L" "=" e
    | "if" b "then" c "else" c
    | c ";" c
    | "while" b "do" c
    | "skip"
b: "true"
    | "false"
    | e "==" e
    | b "&" b
    | "~" b
e: "L"
    | "n"
    | "(" e "+" e ")"
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: {sys.argv[0]} <input-file>")
        exit(1)

    in_file = sys.argv[1]
    parser = Lark(grammar)
    v = parser.parse(open(in_file).read().rstrip())
    exit(0)

if __name__ == '__main__':
    main()

#!/usr/bin/python3
import sys
from lark import Lark


target_grammar = """start: t0
t0: t0 "+" t1
    | t1
t1: t1 "*" t4
    | t4
    | "(" t0 ")"
t2: "1"
    | "2"
    | "3"
    | "4"
    | "5"
    | "6"
    | "7"
    | "8"
    | "9"
t3: "0"
    | t2
t4: t2
    | t4 t3
"""



def main():
    if len(sys.argv) != 2:
        print("Usage: {sys.argv[0]} <input-file>")
        exit(1)

    in_file = sys.argv[1]
    parser = Lark(target_grammar)
    v = parser.parse(open(in_file).read().rstrip())
    exit(0)

if __name__ == '__main__':
    main()

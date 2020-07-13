#!/usr/bin/python3
import sys
from lark import Lark

grammar ="""start: program
program: _stmt_star
stmt: simple_stmt "NEWLINE"
    | "if" expr ":" block _elif_block_star _else_block_one_or_none
    | "while" expr ":" block
    | "for" "ID" "in" expr ":" block
simple_stmt: "pass"
    | expr
    | "return" _expr_one_or_none
    | _target_eq_plus expr
block: "NEWLINE" "INDENT" _stmt_plus "DEDENT"
elif_block: "elif" expr ":" block
else_block: "else" ":" block
expr: cexpr
    | "not" expr
    | expr "and" expr
    | expr "or" expr
    | expr "if" expr "else" expr
cexpr: "ID"
    | literal
    | "[" _exprlist_one_or_none "]"
    | "(" expr ")"
    | member_expr
    | index_expr
    | member_expr "(" _exprlist_one_or_none ")"
    | "ID" "(" _exprlist_one_or_none ")"
    | cexpr bin_op cexpr
    | "~" cexpr
member_expr: cexpr "." "ID"
index_expr: cexpr "[" expr "]"
target: "ID"
    | member_expr
    | index_expr
bin_op: "+"
    | "-"
    | "*"
    | "//"
    | "%"
    | "=="
    | "!="
    | "<="
    | ">="
    | "<"
    | ">"
    | "is"
literal: "None"
    | "True"
    | "False"
    | "INT"
    | "IDSTR"
    | "STR"
exprlist: expr _comma_expr_star
comma_expr: "," expr
target_eq: target "="
_target_eq_plus: _target_eq_plus target_eq
    | target_eq
_stmt_plus: _stmt_plus stmt
    | stmt
_stmt_star: _stmt_star stmt
    |
_elif_block_star: _elif_block_star elif_block
    |
_comma_expr_star: _comma_expr_star comma_expr
    |
_else_block_one_or_none: else_block
    |
_expr_one_or_none: expr
    |
_exprlist_one_or_none: exprlist
    |
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

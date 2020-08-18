import sys
from collections import defaultdict
import re


grammar_line = re.compile("(\[GRAMMAR\] )(.*)")
final_gram_line = re.compile("([mn][0-9]+): (.*)")
grammar = defaultdict(set)
merge_line = re.compile("\[MERGE\] (.*): (.*) == (.*)")
equiv_sets = []
replace_map = {}

def process_grammar_line(line, match):
    outline = match.group(2)
    for key, replace in replace_map.items():
        outline = outline.replace(key, replace)
    m = final_gram_line.match(outline)
    assert(m)
    grammar[m.group(1)].add(m.group(2))

def process_merge_line(line, match):
    first = match.group(2)
    second = match.group(3)
    if equiv_sets:
        for equiv_set in equiv_sets:
            if first in equiv_set:
                if second not in equiv_set:
                    equiv_set.append(second)
                return
            elif second in equiv_set:
                equiv_set.append(first)
                return
    equiv_sets.append([first, second])

def process_merge_sets():
    for i, set in enumerate(equiv_sets):
        replacement = f"m{i}"
        for elem in set:
            replace_map[elem] = replacement


def main():
    grammar_lines = []
    merge_lines = []
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} deserialization-to-fixup")
    for line in open(sys.argv[1]):
        mg = grammar_line.match(line)
        mm = merge_line.match(line)
        if mg is not None:
            grammar_lines.append((line, mg))
        if mm is not None:
            merge_lines.append((line, mm))
    for ml, mm in merge_lines:
        process_merge_line(ml, mm)
    # process_merge_sets()
    print('start: n0')
    nonterminals = 0
    total_productions = 0
    total_nonterm_productions = 0
    for gl, gm in grammar_lines:
        process_grammar_line(gl, gm)
    for rule, prods in grammar.items():
        prods = list(prods)
        print(f"{rule}: {prods[0]}")
        for prod in prods[1:]:
            print(f"    | {prod}")
        nonterm = re.compile("[nm]([0-9]+)")
        is_nonterminal = False
        for prod in prods:
            if nonterm.search(prod) is not None:
                is_nonterminal = True
                break
        if (rule == "n0"):
            total_nonterm_productions += prods[0].count("|") + 1
            total_productions += prods[0].count("|") + 1
        else:
            if is_nonterminal:
                nonterminals += 1
                total_nonterm_productions += len(prods)
            total_productions += len(prods)
  #  print("%%%%%%STATS%%%%%%")
   # print(f"% nonterms: {nonterminals} %")
  #  print(f"% prods: {total_productions} %")
 #   print(f"% nt prods: {total_nonterm_productions} %")
#    print("%%%%%%%%%%%%%%%%%")




if __name__ == "__main__":
    main()

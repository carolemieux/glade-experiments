import sys
from collections import defaultdict
import re


grammar_line = re.compile("(\[GRAMMAR\] )(.*)")
final_gram_line = re.compile("([mn][0-9]+): (.*)")
grammar = defaultdict(set)
merge_line = re.compile("\[MERGE\] (.*): (.*) == (.*)")
equiv_sets = []
equiv_pairs = set()
replace_map = {}
class_strings = {}

def neighbors(node):
    assert(equiv_pairs)
    rets = set()
    for pair in equiv_pairs:
        if pair[0] == node:
            rets.add(pair[1])
    return rets

def degree(node):
    ns = neighbors(node)
    return len(ns)

def bron_kerbosh_2(r, p, x):
    if len(p) == 0 and len(x) == 0:
        equiv_sets.append(r)
        return
    max_degree = max([degree(n) for n in p.union(x)])
    u = [n for n in p.union(x) if degree(n) == max_degree][0]
    for v in p.difference(neighbors(u)):
        bron_kerbosh_2(r.cup({v}), p.intersect(neighbors(v)), x.intersect(neighbors(v)))
        p.remove(v)
        x.add(v)

def verify_equiv_sets():
    for elems in equiv_sets:
        for elem in elems:
            for other_elem in elems.difference({elem}):
                if (elem, other_elem) not in equiv_pairs or (other_elem, elem) not in equiv_pairs:
                    print(f"{elem} and {other_elem} weren't found to be equivalnet")
                    assert(False)


def process_grammar_line(line, match):
    outline = match.group(2)
    for key, replace in sorted(list(replace_map.items()), reverse=True):
        m = re.search(f"({key})[^0-9]", outline)
        while m is not None:
            start, end = m.start(1), m.end(1)
            outline = outline[:start] + replace + outline[end:]
            m = re.search(f"({key})[^0-9]", outline)
    m = final_gram_line.match(outline)
    assert(m)
    rhs = m.group(2)
    alt_node = re.compile("n[0-9]+( \| n[0-9]+)+")
    if alt_node.match(rhs):
        nonterminals = [nt.strip() for nt in rhs.split("|")]
        lhs = m.group(1)
        for nt in nonterminals:
            grammar[lhs].add(nt)
    elif "CCC(" in rhs:
        new_rhs = ''
        start_loc = 0
        par_start_loc = rhs.find("CCC(")
        par_end_loc = rhs.find(")CCC")
        if par_start_loc > 0:
            new_rhs = rhs[:par_start_loc]
        while par_start_loc != -1:
            class_string = rhs[par_start_loc:par_end_loc+4]
            if class_string[3:-3] not in class_strings:
                class_strings[class_string[3:-3]] = f"CLASS{len(class_strings)}"
            new_rhs += class_strings[class_string[3:-3]]
            par_start_loc = rhs.find("CCC(", par_end_loc)
            new_rhs += rhs[par_end_loc+4:(par_start_loc if par_start_loc > 0 else len(rhs))]
            par_end_loc = rhs.find(")CCC", par_start_loc)
        
    #    print(f"old: {rhs}\nnew: {new_rhs}", file = sys.stderr)
        grammar[m.group(1)].add(new_rhs)
    else:
        grammar[m.group(1)].add(m.group(2))

def fixup_merge_nodes():
    def recurses_to_target(target, rep_rule_match):
        def empty_expansion(nt):
            return len(grammar[nt]) == 1 and next(iter(grammar[nt])) == ""
        
        left_c = rep_rule_match.group(1)
        left_empty = empty_expansion(left_c)
        right_c = rep_rule_match.group(3)
        right_empty = empty_expansion(right_c)
        if left_empty and right_empty: 
            return True
        else: return False

    to_remove_dict = defaultdict(list)
    for nt in grammar:
        if nt.startswith('m'):
            to_remove = []
            for exp in grammar[nt]:
                old_len = len(grammar)
                rep_rule_match = re.match(f"([nm][0-9]+) ([nm][0-9]+)\* ([nm][0-9]+)", exp)
                if rep_rule_match:
                    if not rep_rule_match.group(2) == nt: continue
                    if recurses_to_target(nt, rep_rule_match):
                        to_remove.append(exp)
                elif re.match('n[0-9]+', exp):
                   for nt_rule in grammar[exp]:
                        rep_rule_match = re.match(f"([nm][0-9]+) ([nm][0-9]+)\* ([nm][0-9]+)", nt_rule)
                        if rep_rule_match:
                            if recurses_to_target(nt, rep_rule_match):
                                to_remove.append(exp)
            to_remove_dict[nt].extend(to_remove)

    for nt, to_remove in to_remove_dict.items():
        for e in to_remove:
            print("removing ", e, "from ", nt, file=sys.stderr)
            grammar[nt].remove(e)
            grammar[nt].add(f"{nt}*")

def process_merge_line(line, match):
    first = match.group(2)
    second = match.group(3)
    
    equiv_pairs.add((first, second))
    equiv_pairs.add((second, first))

def process_merge_sets():
    nodes_with_merge = set([node for pair in equiv_pairs for node in pair])
    bron_kerbosh_2(nodes_with_merge, set(), set())
    #verify_equiv_sets()
    for i, elems in enumerate(equiv_sets):
        replacement = f"m{i}"
        for elem in elems:
            assert(elem not in replace_map)  # what do we do then?? D:
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
    process_merge_sets()
    print('start: n0')
    nonterminals = 0
    total_productions = 0
    total_nonterm_productions = 0
    for gl, gm in grammar_lines:
        process_grammar_line(gl, gm)
   # fixup_merge_nodes()
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
    for class_string in class_strings:
        print(f"{class_strings[class_string]}: {class_string}")
  #  print("%%%%%%STATS%%%%%%")
   # print(f"% nonterms: {nonterminals} %")
  #  print(f"% prods: {total_productions} %")
 #   print(f"% nt prods: {total_nonterm_productions} %")
#    print("%%%%%%%%%%%%%%%%%")




if __name__ == "__main__":
    main()

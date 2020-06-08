import sys
import re


grammar_line = re.compile("(\[GRAMMAR\] )(.*)")
merge_line = re.compile("\[MERGE\] (.*): (.*) == (.*)")
equiv_sets = []
replace_map = {}

def process_grammar_line(line, match):
    outline = match.group(2)
    outline = outline.replace('"NEWLINE"', "NEWLINE")
    for key, replace in replace_map.items():
        outline = outline.replace(key, replace)
    print(outline)

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
    process_merge_sets()
    print('NEWLINE: "\n"')
    for gl, gm in grammar_lines:
        process_grammar_line(gl, gm)



if __name__ == "__main__":
    main()
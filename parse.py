import sys
import re
import csv
from token_map import token_map

def load_wc(fn):
    fp = open(fn)
    tokens = [line.strip() for line in fp]
    return r"\b(?:%s)\b" % "|".join(tokens)
    
re_parse = re.compile(
    r"""
        (.*?)                 # Medicine
        \s*
        (%(strength)s)\s?       # Strength Extraction
        \s*
        (%(dosage_form)s)    # Dosage form

    """ % {
        "dosage_form" : load_wc("wc_dosageform.txt"),
        "strength" : load_wc("wc_strength.txt"),
    }, 
    re.VERBOSE | re.IGNORECASE
)

def parse(line):
    match = re_parse.search(line)
    if not match:
        raise Exception("Could parse line: " + line)
    return match.groups()

def standardise(tokens):
    stripped = [x.strip() for x in tokens]
    std_tokens = [token_map.get(x, x) for x in stripped]
    return std_tokens

def main(args):
    w = csv.writer(sys.stdout)
    headers = ["medicine name", "strength", "dosage form"]

    w.writerow(headers)
    for line in open(args[1]):
        line = line.strip()
        tokens = parse(line)
        clean_tokens = standardise(tokens)

        w.writerow(clean_tokens)


if __name__ == "__main__":
    main(sys.argv)

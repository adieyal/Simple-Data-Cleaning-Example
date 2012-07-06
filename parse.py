import sys
import re
import csv

def load_wc(fn):
    fp = open(fn)
    tokens = [line.strip() for line in fp]
    return r"\b(?:%s)\b" % "|".join(tokens)
    
re_parse = re.compile(
    r"""
        .*                   # Stuff
        (%(strength)s)       # Strength Extraction
        \s*
        (%(dosage_form)s)    # Dosage form

    """ % {
        "dosage_form" : load_wc("wc_dosageform.txt"),
        "strength" : load_wc("wc_strength.txt"),
    }, 
    re.VERBOSE | re.IGNORECASE
)

def main(args):
    w = csv.writer(sys.stdout)
    headers = ["medicine name", "strength", "dosage form"]

    w.writerow(headers)
    for line in open(args[1]):
        line = line.strip()
        match = re_parse.search(line)
        if not match:
            raise Exception("Could parse line: " + line)
        else:
            w.writerow(["", match.group(1), match.group(2)])


if __name__ == "__main__":
    main(sys.argv)

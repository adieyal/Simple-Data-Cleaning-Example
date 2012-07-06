import sys
import re

def load_wc(fn):
    fp = open(fn)
    tokens = [line.strip() for line in fp]
    return r"\b(?:%s)\b" % "|".join(tokens)
    
re_parse = re.compile(
    r"""
        .*                   # Stuff
        (%(dosage_form)s)    # Dosage form

    """ % {
        "dosage_form" : load_wc("wc_dosageform.txt"),
    }, 
    re.VERBOSE | re.IGNORECASE
)

def main(args):
    for line in open(args[1]):
        line = line.strip()
        match = re_parse.search(line)
        if not match:
            print line
            raise Exception("Could not find dosage form")
        else:
            print match.group(1)


if __name__ == "__main__":
    main(sys.argv)

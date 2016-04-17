# pylint: disable=locally-disabled,missing-docstring

from collections import defaultdict
import re

def max_weight(document):
    weights = defaultdict(int)
    depth = 1
    for tag in re.findall("-?[a-z]", document):
        if tag.startswith("-"):
            depth -= 1
        else:
            weights[tag] += 1 / depth
            depth += 1
    _, _, heaviest_letter = max((weight, -ord(letter), letter) for letter, weight in weights.items())
    return heaviest_letter

def main():
    print(max_weight(input()))


if __name__ == "__main__":
    main()

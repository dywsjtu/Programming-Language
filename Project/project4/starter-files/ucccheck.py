"""
ucccheck.py

Simple check for correct output on a test for the frontend.
"""

import sys
import re

ERROR_PATTERN = re.compile(r'^Error \((\d*)\) at line (\d*): *')

def extract_info(line):
    match = ERROR_PATTERN.match(line)
    return match.group(1, 2) if match else None

def main(filename):
    output = filename.replace('.uc', '.out')
    with open(output) as r, open(output + '.correct') as c:
        results = { extract_info(line) for line in r.readlines()
                    if extract_info(line) }
        correct = { extract_info(line) for line in c.readlines()
                    if extract_info(line) }
        missing = correct - results
        extra = results - correct
        failed = len(missing) + len(extra)
        if missing:
            print('Missing errors:')
            for item in missing:
                print('  Phase {}, line {}'.format(*item))
        if extra:
            print('Extraneous errors:')
            for item in extra:
                print('  Phase {}, line {}'.format(*item))
        if failed:
            print('Test {0} failed.'.format(filename))
            exit(1)
        elif correct:
            print('Test {0} passed.'.format(filename))
            exit(0)

    types = filename.replace('.uc', '.types')
    with open(types) as r, open(types + '.correct') as c:
        if r.read() != c.read():
            print('Error: mismatch detected in types output for ' +
                  filename)
            print(('Run "diff {0} {0}.correct" to see ' +
                   'difference').format(types))
            print('Test {0} failed.'.format(filename))
            exit(1)
        else:
            print('Test {0} passed.'.format(filename))
            exit(0)

if __name__ == '__main__':
    main(sys.argv[1])

#!/usr/bin/env python3

"""
A framework for automating and comparing naive and other solutions.

supply a GENFILE, a python file which will generate the input, or...
supply an INPUTFILE, a file which contains the input.
supply a filepath for the OUTPUTFILE, which will contain the results of testing.
supply a RUNCMDFILE which contains runner commands to be executed, separated by newlines
optionally supply a delimiter (default is "===")
"""

import subprocess
import sys
import argparse
import pathlib
import shlex
from typing import List, Iterator

def get_args():
    parser = argparse.ArgumentParser(description='brutus')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g', nargs='?', type=argparse.FileType('r'), metavar='GENFILE', const='gen.py')
    group.add_argument('-i', nargs='?', type=argparse.FileType('r'), metavar='INPUTFILE', const='input')
    parser.add_argument('-o', nargs='?', type=pathlib.Path, metavar='OUTPUTFILE', const='output')
    parser.add_argument('-s', nargs='?', type=argparse.FileType('r'), metavar='RUNCMDFILE', const='runcmd')
    parser.add_argument('-d', type=str, metavar='DELIMITER', default='===')
    args = parser.parse_args()
    return args

def run_single_testcase(data: str, cmd: List[str]) -> str:
    return subprocess.run(cmd, input=data.encode('utf-8'), stdout=subprocess.PIPE).stdout.decode('utf-8')

def gen_input(genfile: pathlib.Path, delim: str, num_tests=10) -> str:
    res = ''
    for _ in range(num_tests):
        res += subprocess.run(['python', genfile.name], stdout=subprocess.PIPE).stdout.decode('utf-8')
        if not res.endswith('\n'):
            res += '\n'
        res += f'{delim}\n'
    return res

def gen_testcases(lines: str, delim: str) -> Iterator[str]:
    test_case_token = ''
    for line in lines.split('\n'):
        if line == delim:
            data = test_case_token
            yield data
            test_case_token = ''
        else:
            test_case_token += f'{line}\n'

    if test_case_token.strip() != '':
        data = test_case_token
        yield data

def main(args: argparse.Namespace):

    GENFILE = args.g
    INPUTFILE = args.i
    OUTPUTFILE = args.o
    RUNCMDFILE = args.s
    DELIMITER = args.d

    #
    # get run commands
    #

    run_cmds = list(map(shlex.split, RUNCMDFILE.readlines()))
    print(run_cmds)

    #
    # get input data
    #

    test_input = "Nothing to see here."

    if GENFILE is not None:
        test_input = gen_input(GENFILE, DELIMITER)
    elif INPUTFILE is not None:
        test_input = INPUTFILE.read()
    else:
        sys.exit('no method of input given')

    #
    # generate output data
    #

    with open(OUTPUTFILE, 'w+') as outputfile:
        for testcase in gen_testcases(test_input, DELIMITER):
            outputfile.write(f'{DELIMITER} BEGIN INPUT {DELIMITER}\n{testcase}\n{DELIMITER} END INPUT {DELIMITER}\n')

            for rc in run_cmds:
                outputfile.write(f'{DELIMITER} {rc}:\n')
                output = run_single_testcase(testcase, rc)
                if not output.endswith('\n'):
                    output += '\n'
                outputfile.write(output)

if __name__ == '__main__':
    args = get_args()
    main(args)

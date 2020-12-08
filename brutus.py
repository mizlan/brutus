#!/usr/bin/env python3

"""
A framework for automating and comparing naive and other solutions

One single file can be used for all testcases, with single line of "==="
denoting a testcase separator.
"""

import subprocess
import sys
import argparse
import pathlib
import io
from typing import IO, List

def get_args():
    parser = argparse.ArgumentParser(description='brutus')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g', type=argparse.FileType('r'), metavar='GENFILE', default='gen.py')
    group.add_argument('-i', type=argparse.FileType('r'), metavar='INPUTFILE', default='input')
    parser.add_argument('-o', type=pathlib.Path, metavar='OUTPUTFILE', default='output')
    parser.add_argument('-s', type=argparse.FileType('r'), metavar='SRCFILE')
    parser.add_argument('-d', type=argparse.FileType('r'), metavar='DELIMITER', default='===')
    args = parser.parse_args()
    return args

def run_single_testcase(stream: IO, cmd: List[str]) -> str:
    return subprocess.run(cmd, stdin=stream, stdout=subprocess.PIPE).stdout.decode('utf-8')

def gen_input(genfile: pathlib.Path, args: argparse.Namespace, num_tests=3) -> str:
    res = ''
    for _ in range(num_tests):
        res += subprocess.run(['python', genfile.name], stdout=subprocess.PIPE).stdout.decode('utf-8')
        if not res.endswith('\n'):
            res += '\n'
        res += f'{args.d}\n'
    return res

def main(args: argparse.Namespace):

    #
    # get input data
    #

    test_input = "Nothing to see here."

    if args.g is not None:
        test_input = gen_input(args.g, args.d)
    elif args.i is not None:
        test_input = args.i.read()
    else:
        sys.exit('no method of input given')

    #
    # generate output data
    #

    test_case_token = ''
    for line in test_input.split('\n'):
        if line == args.d:



if __name__ == '__main__':
    args = get_args()
    main(args)

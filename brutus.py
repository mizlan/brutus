#!/usr/bin/env python3

"""
A framework for automating and comparing naive and other solutions

One single file can be used for all testcases, with single line of "==="
denoting a testcase separator.
"""

import subprocess
import argparse
# import pathlib
from typing import IO, List

def get_args():
    parser = argparse.ArgumentParser(description='brutus')
    parser.add_argument('-g', type=argparse.FileType('r'), metavar='GENFILE')
    parser.add_argument('-i', type=argparse.FileType('r'), metavar='INPUTFILE')
    args = parser.parse_args()
    return args

def run_single_testcase(stream: IO, cmd: List[str]) -> str:
    return subprocess.run(cmd, stdin=stream, stdout=subprocess.PIPE).stdout.decode('utf-8')

def main(args: argparse.Namespace):
    print(args)

if __name__ == '__main__':
    args = get_args()
    main(args)

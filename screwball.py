#!/usr/bin/env python3

import argparse

def load_dict(dict):
    words = []
    return words

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dict', type=str, default='/usr/share/dict/words')
    parser.add_argument()
    args=parser.parse_args()
    dict = args.dict
    words = load_dict(dict)

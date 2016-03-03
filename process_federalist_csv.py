'''Regularize federalist.csv's odd conventions.

``federalist.csv`` uses some odd conventions. For example, it encodes commas as
'<c>'. This script restores the originals.

'''

import os

import pandas as pd


ORIGINALS_DIR = 'originals'
DERIVATIVES_DIR = 'derivatives'


def main():
    df = pd.read_csv(os.path.join(ORIGINALS_DIR, 'federalist.csv'), index_col=0)
    df.index.name = 'code_number'
    df.columns = ['AUTHOR', 'text']
    df['text'] = df['text'].str.replace(r'\s*<\w+>\s*', ' ')
    df.to_csv(os.path.join(DERIVATIVES_DIR, 'federalist.csv'))


if __name__ == '__main__':
    main()

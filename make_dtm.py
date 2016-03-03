import os
import re

import pandas as pd
import sklearn.feature_extraction.text


DERIVATIVES_DIR = 'derivatives'


def main():
    df_federalist = pd.read_csv(os.path.join(DERIVATIVES_DIR, 'federalist.csv'), index_col=0)
    texts = df_federalist.text.tolist()
    code_numbers = df_federalist.index.tolist()
    authors = df_federalist['AUTHOR'].tolist()
    del df_federalist
    for filename in os.listdir(DERIVATIVES_DIR):
        if 'madison' not in filename:
            continue
        match = re.search(r'code([0-9]+)', filename)
        assert match, filename
        code_numbers.append(int(match.groups()[0]))
        authors.append('MADISON')
        with open(os.path.join(DERIVATIVES_DIR, filename)) as f:
            texts.append(f.read())
    vec = sklearn.feature_extraction.text.CountVectorizer(token_pattern=r'(?u)\b\w+\b')
    dtm = pd.DataFrame(vec.fit_transform(texts).toarray(),
                       columns=vec.get_feature_names(),
                       index=code_numbers)
    dtm['AUTHOR'] = authors
    dtm.to_csv('mosteller-wallace-federalist-papers.csv')


if __name__ == '__main__':
    main()

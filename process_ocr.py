'''Recover approximations of Mosteller and Wallace's corpus from OCR.

See p. 269-270 in Mosteller and Wallace 1964 for the relevant details.
'''

import os
import re

import madison_rules


ORIGINALS_DIR = 'originals/ocr'
DERIVATIVES_DIR = 'derivatives'

def _process_ocr_subtask(filename, clean_pats, split_pats):
    with open(os.path.join(ORIGINALS_DIR, filename)) as f:
        lines = f.readlines()

    # remove running headers
    lines_to_remove = set()
    for i, line in enumerate(lines):
        for regex in clean_pats:
            if re.search(regex, line):
                lines_to_remove.add(i)
    lines = [line for i, line in enumerate(lines) if i not in lines_to_remove]

    # split out component chunks
    for key, (start_re, stop_re) in split_pats.items():
        writing = False
        chunk = []
        for line in lines:
            if re.search(start_re, line):
                assert not writing, line
                writing = True
                chunk.append(line)
                continue
            if writing:
                chunk.append(line)
                if re.search(stop_re, line):
                    break
        assert writing, 'Did not find starting regular expression: `{}`'.format(start_re)
        assert len(chunk) > 0, (key, start_re, stop_re)
        assert sum(len(line.split()) for line in chunk) < 5000, 'Did not find ending regular expression in `{}`'.format(stop_re)
        with open(os.path.join(DERIVATIVES_DIR, '{}.txt'.format(key)), 'w') as f:
            f.writelines(chunk)

def _merge_subtask(merge_rules):
    for target, sources in merge_rules.items():
        parts = []
        for source in sources:
            source_fn = os.path.join(DERIVATIVES_DIR, '{}.txt'.format(source))
            with open(source_fn) as f:
                parts.append(f.read())
            os.remove(source_fn)
        with open(os.path.join(DERIVATIVES_DIR, '{}.txt'.format(target)), 'w') as f:
            f.writelines(parts)


def main():
    _process_ocr_subtask(madison_rules.hunt_v6_filename,
                         madison_rules.hunt_v6_clean,
                         madison_rules.hunt_v6_split)
    _merge_subtask(madison_rules.hunt_v6_merge)
    _process_ocr_subtask(madison_rules.hunt_v7_filename,
                         madison_rules.hunt_v7_clean,
                         madison_rules.hunt_v7_split)
    _merge_subtask(madison_rules.hunt_v7_merge)


if __name__ == '__main__':
    main()

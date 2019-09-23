import argparse

import pandas as pd
from pathlib import Path

METRIC = 'PR-AUC-macro'


def pretty(df: pd.DataFrame):
    return df.style.format("{:.3f}").render()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate leaderboard tables')
    parser.add_argument('directory', help='directory with results in TSV file per team')
    parser.add_argument('output', help='output markdown file')
    args = parser.parse_args()

    root = Path(args.directory)
    tsv_files = root.glob('./*.tsv')
    results = {}
    best = {}
    for tsv_file in tsv_files:
        team = tsv_file.stem
        data = pd.read_csv(tsv_file, delimiter='\t', index_col=0)
        results[team] = data

        value = data[METRIC].max()
        run_name = data[METRIC].idxmax()

        best['{} ({})'.format(team, run_name)] = value

    best = pd.DataFrame(best.values(), best.keys(), columns=[METRIC])

    output = '## Leaderboard\n\n'
    output += pretty(best) + '\n\n'
    output += '## All submissions\n\n'

    for team, result in results.items():
        output += '### ' + team + '\n\n'
        output += pretty(result) + '\n\n'

    with open(args.output, 'w') as fp:
        fp.write(output)

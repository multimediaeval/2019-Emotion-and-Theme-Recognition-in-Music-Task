import argparse

import pandas as pd
from pathlib import Path

METRIC = 'PR-AUC-macro'
METRICS = ['PR-AUC-macro', 'ROC-AUC-macro']


def pretty(df: pd.DataFrame):
    return df.style.render()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate leaderboard tables')
    parser.add_argument('directory', help='directory with results in TSV file per team')
    parser.add_argument('output', help='output markdown file')
    args = parser.parse_args()

    root = Path(args.directory)
    tsv_files = root.glob('./*.tsv')
    results = {}
    leaderboard = None
    for tsv_file in tsv_files:
        team = tsv_file.stem
        data = pd.read_csv(tsv_file, delimiter='\t', index_col=0)
        results[team] = data

        data_slice = data[METRICS]
        data_slice.insert(0, 'Team', team)

        if leaderboard is None:
            leaderboard = data_slice
        else:
            leaderboard = pd.concat([leaderboard, data_slice])

    leaderboard = leaderboard.sort_values(by=METRIC, ascending=False)
    leaderboard.insert(1, 'Run', leaderboard.index)
    leaderboard.reset_index(inplace=True, drop=True)
    leaderboard.index += 1

    output = '## Leaderboard\n\n'
    output += pretty(leaderboard) + '\n\n'
    output += '## All submissions\n\n'

    for team, result in results.items():
        output += '### ' + team + '\n\n'
        output += pretty(result) + '\n\n'

    with open(args.output, 'w') as fp:
        fp.write(output)

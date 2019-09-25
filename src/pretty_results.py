import argparse
from pathlib import Path
import json

import pandas as pd
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt


def leaderboard(df: pd.DataFrame, by):
    df = df.sort_values(by=by, ascending=False)
    df.reset_index(inplace=True, drop=True)
    df.index += 1
    return df.style.render()


def plot(data, x_name, y_name, filename):
    plt.figure(figsize=[10, 8])
    ax = sns.scatterplot(x=x_name, y=y_name, hue='Team', data=data)
    for _, row in data.iterrows():
        plt.text(row[x_name], row[y_name] + 0.003, row['Run'], fontsize=8, horizontalalignment='center')
    # ax.set_xlim(0,)
    # ax.set_ylim(0,)
    plt.savefig(filename, bbox_inches='tight')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate leaderboard tables')
    parser.add_argument('directory', help='directory with results in TSV file per team')
    parser.add_argument('output', help='output markdown file')
    args = parser.parse_args()

    root = Path(args.directory)
    tsv_files = root.glob('./*.tsv')
    results = {}
    data_all = None
    for tsv_file in sorted(tsv_files):
        team = tsv_file.stem
        data = pd.read_csv(tsv_file, delimiter='\t', index_col=0)
        results[team] = data

        data_slice = data[['PR-AUC-macro', 'ROC-AUC-macro', 'precision-macro', 'recall-macro', 'F-score-macro']]
        data_slice.insert(0, 'Team', team)
        data_slice.insert(0, 'N', range(1, len(data_slice)+1))

        if data_all is None:
            data_all = data_slice
        else:
            data_all = pd.concat([data_all, data_slice])

    data_all.insert(1, 'Run', data_all.index)

    output = '# Submission results\n\n'
    output += '## Leaderboard - PR-AUC-macro\n\n'
    output += leaderboard(data_all[['Team', 'Run', 'PR-AUC-macro', 'ROC-AUC-macro']], by='PR-AUC-macro') + '\n\n'

    plot(data_all, 'recall-macro', 'precision-macro', '../img/precision-recall.svg')
    # plot(data_all, 'ROC-AUC-macro', 'PR-AUC-macro', '../img/roc-pr.svg')

    output += '## Leaderboard - F-score-macro\n\n'
    output += leaderboard(data_all[['Team', 'Run', 'F-score-macro']], by='F-score-macro') + '\n\n'

    output += '## Precision vs recall\n\n'
    output += '<img src="img/precision-recall.svg"/>\n\n'

    # output += '## PR-AUC-macro vs ROC-AUC-macro\n\n'
    # output += '<img src="img/roc-pr.png"/>\n\n'

    with (root / 'sources.json').open() as fp:
        sources = json.load(fp)

    output += '## All submissions\n\n'
    for team, result in results.items():
        output += '### ' + team + '\n\n'
        if team in sources:
            output += 'Source code: ' + ', '.join(['[{url}]({url})'.format(url=url) for url in sources[team]]) + '\n\n'
        output += result.style.render() + '\n\n'

    with open(args.output, 'w') as fp:
        fp.write(output)

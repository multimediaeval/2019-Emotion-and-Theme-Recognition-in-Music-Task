import argparse
from pathlib import Path

import numpy as np
import pandas as pd

from evaluate import evaluate


def extract_run_name(path):
    run_name = str(path).split(team_name)[1][:-15].strip('-_ /')
    if '/' in run_name:
        run_name = run_name.split('/')[0]
    if not run_name:
        run_name = ' '
    return run_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run evaluation for all teams')
    parser.add_argument('submissions_dir', help='directory with each team submission directory containing prediction '
                                                'and decision files')
    parser.add_argument('results_dir', help='directory with results TSV files per team')
    parser.add_argument('groundtruth', help='groundtruth NPY file')
    args = parser.parse_args()

    groundtruth = np.load(args.groundtruth)

    submissions_dirs = [d for d in Path(args.submissions_dir).iterdir() if d.is_dir()]

    for team_dir in submissions_dirs:
        results = {}
        team_name = team_dir.stem
        prediction_files = sorted(team_dir.glob('**/*predictions.npy'))
        decision_files = sorted(team_dir.glob('**/*decisions.npy'))

        # get the name of algorithm that might be either prefix on filename or a directory
        run_names = [extract_run_name(path) for path in prediction_files]

        for name, prediction_file, decision_file in zip(run_names, prediction_files, decision_files):
            try:
                predictions = np.load(prediction_file)
                decisions = np.load(decision_file)
                results[name] = evaluate(groundtruth, predictions, decisions)
            except ValueError as e:
                print(e)

        if results:
            df = pd.DataFrame(results).T
            df.to_csv(Path(args.results_dir) / (team_name + '.tsv'), sep='\t', float_format='%.6f')

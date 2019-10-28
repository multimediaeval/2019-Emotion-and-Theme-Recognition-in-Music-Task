from pathlib import Path

import numpy as np

from evaluate import evaluate

RUNS = [
    # 'CP-JKU/3_avg_ensemble/',
    'AMLAG/submission2/',
    'YL-UTokyo/run1/',
    'AugLi/all-',
    'TaiInn (Innsbruck)/run_2_',
    'baseline/vggish_'
]


def main():
    root = Path('../submissions')
    data_avg = None

    for run in RUNS:
        data = np.load(root / (run + 'predictions.npy'))
        print(f'{run:24} {data.min():.6} ~ {data.max()}, mean={data.mean()}, std={data.std()}')
        data = (data - data.mean()) / (data.std())
        data_avg = data if data_avg is None else data_avg + data

    data_avg /= len(RUNS)
    evaluate(np.load('groundtruth.npy'), data_avg, np.zeros(data_avg.shape, dtype=bool), display=True)


if __name__ == '__main__':
    main()

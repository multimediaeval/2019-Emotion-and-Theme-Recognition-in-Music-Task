#!/usr/bin/env bash
cd src
python evaluate_all.py ../submissions ../submissions groundtruth.npy
python pretty_results.py ../submissions ../results.md

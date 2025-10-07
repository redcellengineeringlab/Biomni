#! /bin/bash
set -e

cd generated_files
exec conda run --live-stream -n biomni_e1 python -u ../main.py

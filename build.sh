#!/bin/bash

rm -r dist
python -m hatchling build
# python -m twine upload dist/*
# pip install --force-reinstall dist/*.whl
cp dist/*.whl /mnt/ssd

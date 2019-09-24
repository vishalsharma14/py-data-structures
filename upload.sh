#!/bin/bash
rm -r dist/
python3 setup.py sdist
python3 -m twine check dist/*
python3 -m twine upload dist/*
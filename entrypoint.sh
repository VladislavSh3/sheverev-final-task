#!/bin/sh

if [ $1 = "test" ]; then
  python -m unittest tests.py
fi

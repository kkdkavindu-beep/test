# Rubik's Cube Solving Web App (Python)

A small Flask web app with a UI that accepts a Rubik's cube scramble and returns a solving sequence.

## What this solver does

This app computes the **inverse of a scramble algorithm**, which solves cubes that were scrambled from solved state using the provided sequence.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open http://localhost:8000.

## Input format

- Space-separated moves, like: `R U R' U' F2 D`
- Supported faces: `U D L R F B`
- Supported suffixes: none, `'`, `2`

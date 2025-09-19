#!/usr/bin/env bash
python3 -m pip install --user pytest >/dev/null 2>&1 || true
pytest -q tests/unit || exit 1

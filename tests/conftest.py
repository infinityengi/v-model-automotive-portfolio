# tests/conftest.py
import os
import sys

# Add repo root to sys.path so tests can import the project package 'code'
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

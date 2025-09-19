"""
Top-level package for project code.

Warning: avoid naming packages 'code' in the long term because it shadows
Python's standard library module `code` (used by pdb). Consider renaming
this package to a project-specific name (e.g., 'infinityengi' or 'src').
"""
__all__ = []
# make package
# from project root
test -d code && test -f code/perception.py && touch code/__init__.py || echo "Either code/ or code/perception.py missing"

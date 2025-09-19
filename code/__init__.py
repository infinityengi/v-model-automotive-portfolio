# make package
# from project root
test -d code && test -f code/perception.py && touch code/__init__.py || echo "Either code/ or code/perception.py missing"

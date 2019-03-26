import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    date = input()
    if date == "OCT 31" or date == "DEC 25": print("yup")
    else: print("nope")

main()

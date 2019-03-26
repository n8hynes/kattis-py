import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    if "ss" in line: print("hiss")
    else: print("no hiss")

main()

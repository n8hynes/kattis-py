import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    # Solve problem here

main()

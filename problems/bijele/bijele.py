import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    pieces_have = [int(x) for x in line.split()]
    pieces_need = [1, 1, 2, 2, 2, 8]
    for x in range(6):
        pieces_need[x] -= pieces_have[x]
    print(*pieces_need, sep=" ")

main()

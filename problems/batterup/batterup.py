import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(sys.stdin.readline())
    at_bats = [int(x) for x in sys.stdin.readline().split()]
    num = 0
    den = len(at_bats)
    for x in at_bats:
        if (x == -1):
            den -= 1
        else:
            num += x
    score = num / den
    print(score)


main()

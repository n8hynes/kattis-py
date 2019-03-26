import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(input())
    for _ in range(n):
        r, e, c = [ int(x) for x in input().split() ]
        if e - c > r:
            print("advertise")
        elif e - c == r:
            print("does not matter")
        else:
            print("do not advertise")

main()

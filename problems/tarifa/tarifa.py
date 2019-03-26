import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    X = int(sys.stdin.readline())
    N = int(sys.stdin.readline())
    data = X * N
    for _ in range(N):
        data -= int(sys.stdin.readline())
    print(data + X)

main()

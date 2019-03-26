import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def main():
    L = int(sys.stdin.readline())
    D = int(sys.stdin.readline())
    X = int(sys.stdin.readline())
    
    for i in range(L, D + 1):
        if sum_digits(i) == X:
            N = i
            break
    print(N)

    for i in reversed(range(L, D + 1)):
        if sum_digits(i) == X:
            M = i
            break
    print(M)


main()

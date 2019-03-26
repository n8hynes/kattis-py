import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    n = int(line)
    quality = 0
    for _ in range(n):
        q, y = sys.stdin.readline().split()
        q = float(q)
        y = float(y)
        quality += q * y
    print(f"{quality:.3f}")

main()

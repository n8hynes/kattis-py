import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    c = float(sys.stdin.readline())
    n = int(sys.stdin.readline())
    total_area = 0
    for _ in range(n):
        line = sys.stdin.readline()
        x,y = line.split()
        x = float(x)
        y = float(y)
        total_area += x * y
    cost = total_area * c
    print(f"{cost:.7f}")

main()

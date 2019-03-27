import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(input())
    days = [ False for _ in range(365) ]
    for _ in range(n):
        s, t = [ int(x) for x in input().split() ]
        for i in range(s - 1, t):
            days[i] = 1
    count = 0
    for day in days:
        if day:
            count += 1
    print(count)

main()

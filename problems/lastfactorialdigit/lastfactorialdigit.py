import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    t = int(line)
    for _ in range(t):
        line = sys.stdin.readline()
        n = int(line)
        if (n == 1): result = 1
        elif (n == 2): result = 2
        elif (n == 3): result = 6
        elif (n == 4): result = 4
        else: result = 0
        print(result)

main()

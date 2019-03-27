import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = input()
    A, B = line.split()
    A = int(A[::-1])
    B = int(B[::-1])
    if A > B: print(A)
    else: print(B)

main()

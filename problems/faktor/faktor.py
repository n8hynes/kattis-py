import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

"""
Calculates the number of citations needed to get a certain inpact factor
Impact factor determined by the formula:
    I = C / A
    where I = Impact factor
    C = Citations received
    A = Articles published
"""
def main():
    line = sys.stdin.readline()
    a, i = (int(x) for x in line.split())
    c = a * i - a + 1
    print(c)

main()

import sys
import math

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    n = int(sys.stdin.readline())
    points=4
    squares=1
    for i in range(1,n+1):
        points += squares*3 #center/top/left of each square
        points += int(math.sqrt(squares))*2 #bottom/right edges
        squares *= 4
    print(points)

main()

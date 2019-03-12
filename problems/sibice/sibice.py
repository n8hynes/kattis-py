import sys
import math

def main():
    line = sys.stdin.readline()
    n, w, h = (int(x) for x in line.split())
    d = math.sqrt(w*w+h*h)
    for _ in range(n):
        match = int(sys.stdin.readline())
        if (match > d):
            print("NE")
        else:
            print("DA")
main()

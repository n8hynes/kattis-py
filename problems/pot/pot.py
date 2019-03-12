import sys

def main():
    n = int(sys.stdin.readline())
    sum = 0
    for _ in range(n):
        num = int(sys.stdin.readline())
        pow = num % 10
        num = int(num / 10)
        sum = sum + num ** pow
    print(sum)

main()

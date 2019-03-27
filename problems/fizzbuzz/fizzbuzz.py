import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = input()
    X, Y, N = [ int(x) for x in line.split() ]
    for n in range(1, N + 1):
        if (n % X == 0) and (n % Y == 0): print("FizzBuzz")
        elif (n % X == 0): print("Fizz")
        elif (n % Y == 0): print("Buzz")
        else:
            print(n)

main()

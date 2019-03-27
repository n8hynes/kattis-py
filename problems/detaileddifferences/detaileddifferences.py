import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        line_1 = input()
        line_2 = input()
        diff = ''
        for i in range(len(line_1)):
            if line_1[i] == line_2[i]: diff += '.'
            else: diff += '*'
        print(line_1)
        print(line_2)
        print(diff)
        print()

main()

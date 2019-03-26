import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    english_miles = float(sys.stdin.readline())
    roman_miles = english_miles * 5280 / 4854 * 1000
    print(round(roman_miles))

main()

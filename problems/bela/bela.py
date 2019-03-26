import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def get_card_value(val, suit, dominant):
    if (suit == dominant):
        if (val == 'J'): return 20
        elif (val == '9'): return 14
    if (val == 'A'): return 11
    elif (val == 'K'): return 4
    elif (val == 'Q'): return 3
    elif (val == 'J'): return 2
    elif (val == 'T'): return 10
    elif (val == '9' or val == '8' or val == '7'): return 0

def main():
    line = sys.stdin.readline()
    n, b = line.split()
    n = int(n)
    points = 0
    for _ in range(4 * n):
        card = sys.stdin.readline()
        points += get_card_value(card[0], card[1], b)
    print(points)


main()

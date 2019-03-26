import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    line = sys.stdin.readline()
    initials = ''
    for char in line:
        if char.isupper(): initials += char
    print(initials)

main()

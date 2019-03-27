import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    N = int(input())
    for _ in range(N):
        b, p = input().split()
        b = int(b)
        p = float(p)

        max_t = p / (b+1)
        min_t = p / (b-1)
        min_abpm = 60 / min_t
        bpm = 60 * b / p
        max_abpm = 60 / max_t

        print(f'{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}')




main()

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def check_phone_nums(x, y):
    if (x.find(y) == 0) or (y.find(x) == 0): return False
    else: return True

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        num_list = []
        consistent = True
        for __ in range(n):
            num = sys.stdin.readline().rstrip()
            for x in num_list:
                # eprint(f"Checking {x} vs {num}: {check_phone_nums(x,num)}")
                if not check_phone_nums(x,num): consistent = False
            num_list.append(num)
        if consistent: print("YES")
        else: print("NO")


main()


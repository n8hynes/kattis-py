import sys
import itertools

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def consistency_check(num_1, num_2):
    """ 
    Checks if 2 phone numbers are inconsistent.
    Requires len(num_1) <= len(num_2)
    """
    if (num_2[:len(num_1)] == num_1): return False
    else: return True

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        num_list = []
        consistent = True
        for __ in range(n):
            new_num = sys.stdin.readline().rstrip()
            num_list.append(new_num)
        num_list.sort(key = len)
        consistent = True
        for pair in itertools.product(num_list, repeat=2):
            if (pair[0] == pair[1]) or (len(pair[0]) > len(pair[1])): continue
            # eprint(f"Checking {pair}")
            if consistency_check(*pair) == False:
                consistent = False
                break
        if(consistent): print("YES")
        else: print("NO")

main()


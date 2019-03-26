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

def check_num_list(nums):
    """
    Checks each pair of items in the list for consistency.
    """
    consistent = True
    nums.sort(key = len)
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if not consistency_check(nums[x], nums[y]):
                consistent = False
                break
        if not consistent: break
    return consistent


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        num_list = [[] for x in range(10)]
        consistent = True
        for _ in range(n):
            new_num = sys.stdin.readline().rstrip()
            num_list[int(new_num[0])].append(new_num)
        for bucket in num_list:
            consistent = check_num_list(bucket)
            if not consistent: break
        if consistent: print("YES")
        else: print("NO")
            
            

main()


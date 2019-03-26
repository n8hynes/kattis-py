import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = []
        for _ in range(n):
            nums.append(input())
        nums = sorted(nums, key=len, reverse=True)
        d = set()
        consistent = True
        for num in nums:
            if not consistent: break
            if num in d:
                consistent = False
                break
            for i in range(1, len(num)+1):
                d.add(num[:i])

        if consistent: print("YES")
        else: print("NO")
 

main()


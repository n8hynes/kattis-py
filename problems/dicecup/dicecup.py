import sys

def main():
    line = sys.stdin.read()
    n, m = line.split()
    n = int(n)
    m = int(m)
    outcomes=[]
    for i in range(1,n+1):
        for j in range(1,m+1):
            outcomes.append(i + j)
    most_likely = 0
    final_list=[]
    for i in range(2,n + m + 1):
        if outcomes.count(i) > most_likely:
            most_likely = outcomes.count(i)
            final_list.clear()
            final_list.append(i)
        elif outcomes.count(i) == most_likely:
            if i not in final_list: final_list.append(i)
    for i in final_list:
        print(i)

main()

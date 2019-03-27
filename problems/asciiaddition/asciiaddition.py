import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

nums = [[] for _ in range(11)]
nums[0] =  ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx']
nums[1] =  ['....x','....x','....x','....x','....x','....x','....x']
nums[2] =  ['xxxxx','....x','....x','xxxxx','x....','x....','xxxxx']
nums[3] =  ['xxxxx','....x','....x','xxxxx','....x','....x','xxxxx']
nums[4] =  ['x...x','x...x','x...x','xxxxx','....x','....x','....x']
nums[5] =  ['xxxxx','x....','x....','xxxxx','....x','....x','xxxxx']
nums[6] =  ['xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx']
nums[7] =  ['xxxxx','....x','....x','....x','....x','....x','....x']
nums[8] =  ['xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx']
nums[9] =  ['xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx']
nums[10] = ['.....','..x..','..x..','xxxxx','..x..','..x..','.....']


def get_character(char):
    for x in range(11):
        if char == nums[x]: 
            if x == 10: return '+'
            else: return str(x)

def to_matrix(num):
    output = ['' for _ in range(7)]
    for digit in str(num):
        index = int(digit)
        for x in range(7):
            output[x] += nums[index][x] + '.'
    for x in range(7):
        output[x] = output[x][:-1]
    return output


def main():
    problem_matrix = []
    for _ in range(7):
        problem_matrix.append(input())
    line_length = len(problem_matrix[0])
    char_total = int((line_length + 1) / 6)
    problem_string = ''
    for _ in range(char_total):
        char = []
        for i in range(7):
            char.append(problem_matrix[i][:5])
            problem_matrix[i] = problem_matrix[i][6:]
        problem_string += get_character(char)
    a, b = problem_string.split('+')
    result = int(a) + int(b)
    print(*to_matrix(result), sep='\n')
    

main()

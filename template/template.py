import sys

def solve(): 
    return 1

def main():
    for T in range(1, int(input())+1):
        N = int(input())
        inp = list(map(int, input().split()))
        out = solve(inp)
        caseStr="Case #%s: %s" % (T, out) 
        print(caseStr)

print(solve([5,6,8,4,3]))
print(solve([8,9,7]))

#sys.stdin = open('input.txt', 'r')
#main()
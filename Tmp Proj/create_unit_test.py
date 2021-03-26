#https://code.google.com/codejam/contest/dashboard?c=3264486#s=p0
import os
import math
import random

def rand(maxS):
    lenS=random.randint(2, maxS)    #rand string len
    S=''.join(map(lambda x: random.choice('-+'), range(lenS)))  #pop S with random chars
    K=random.randint(2, lenS)       #rand K
    return S,K
               
def create_test_file(T,maxS):
    file="A-large-attempt0"                     #filename
    with open(file+'.in', 'wt') as outfile:
        print(str(T))
        outfile.write(str(T)+"\n")
        for t in range(1, T+1):
            S,K = rand(maxS)
            casestr="%s %s\n" % (S,K)
            #casestr="Case #%s: %s %s\n" % (case,out[0],out[1])
            print(casestr)
            outfile.write(casestr)
                
create_test_file(100,1000)
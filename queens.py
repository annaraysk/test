#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, rq, cq, obs):
    
    ans=0
    for i in range(rq,n+1):
        if [i,cq] in obs:
            break
        ans+=1
    for i in range(min(rq-n,cq-n)):
        if [rq+i+1,cq+i+1] in obs:
            break
        ans+=1
    for i in range(cq,n+1):
        if [rq,i] in obs:
            break
        ans+=1
    for i in range(min(abs(rq-1),abs(cq-n))):
        if [rq-i-1,cq+i+1] in obs:
            break
        ans+=1
    for i in range(rq,0,-1):
        if [i,cq] in obs:
            break
        ans+=1
    for i in range(min(abs(rq-1),abs(cq-1))):
        if [rq-i-1,cq-i-1] in obs:
            break
        ans+=1
    for i in range(cq,0,-1):
        if [rq,i] in obs:
            break
        ans+=1
    for i in range(min(abs(rq-1),abs(cq-1))):
        if [rq+i+1,cq-i-1] in obs:
            break
        ans+=1
        
    return ans
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()

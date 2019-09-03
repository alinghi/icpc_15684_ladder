import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")
table=[[False]*(12) for _ in range(31)]

def init():
    N, M, H = map(int,input().split())
    #dummy
    for i in range(M):
        a,b=map(int,input().split())
        table[a][b]=True
    return N,M,H,table

def ladder(table,N,H):
    for j in range(1,N):
        k=j
        for i in range(1,H+1):
            if table[i][k]:
                k+=1
            elif table[i][k-1]:
                k-=1
        if j!=k:
            return False
    return True

def resolver(table,N,H,aim,cnt):
    if aim==cnt:
        return ladder(table,N,H)
    for i in range(H+1):
        for j in range(1,N):
            if table[i][j-1] or table[i][j] or table[i][j+1]:
                continue
            table[i][j]=True
            if resolver(table, N, H, aim, cnt+1):
                return True
            table[i][j] = False
    return False
def solver(N,H,table):
    for i in range(4):
        if resolver(table, N, H, i, 0):
            return i
    return -1

N,M,H,table=init()
print(solver(N,H,table))
'''

给定一个N*M的矩阵，在矩阵中每一块有一张牌，我们假定刚开始的时候所有牌的牌面向上。
现在对于每个块进行如下操作：
> 翻转某个块中的牌，并且与之相邻的其余八张牌也会被翻转。
XXX
XXX
XXX
如上矩阵所示，翻转中间那块时，这九块中的牌都会被翻转一次。
请输出在对矩阵中每一块进行如上操作以后，牌面向下的块的个数。
'''

t = int(input())
for i in range(t):
    A = list(map(int,input().split()))   # 数学规律题
    N, M = A[0], A[1]
    if N == 1 and M == 1:
        print(1)
    elif N == 1 or M == 1:  # 一行N列或者一列N行都是一样的，他们的相邻元素都是有相同的规律
        if N == 1:
            print(M-2)
        else:
            print(N-2)
    else:                     # N行M列则可以看做1行M列的一个累加
        print((N-2)*(M-2))
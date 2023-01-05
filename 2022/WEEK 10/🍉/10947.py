
# def dfs():
#     if len(arr) == n:
#         print(*arr,sep=' ')

#     for i in range(1,n+1):
#         if i not in arr:
#             arr.append(i)
#             dfs()
#             arr.pop()

# n=int(input())
# arr = []

# dfs()   
    
# from itertools import permutations

# n = int(input())
# arr = [i for i in range(1, n + 1)]
# for i in permutations(arr, n):
#     print(*i)
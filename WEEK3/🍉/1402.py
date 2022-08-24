k = int(input())
arr = input().split()[:k]


while(len(arr)):
   print(arr.pop(),end=' ')
   
#print(' '.join(arr[::-1]))
#print(' '.join(reversed(arr)))
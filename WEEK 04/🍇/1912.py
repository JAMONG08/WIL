def rec(n):
  if(n > 1):
    n * rec(n-1)
  else:
    return n
  
  
num = int(input())
last = rec(num)

print(last)

# import os


# currentpath = os.getcwd()   # 현재 실행하는 파일 경로
# print(currentpath)

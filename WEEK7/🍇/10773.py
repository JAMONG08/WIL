N = int(input())
sum = 0
stack = []

for i in range(N):
  num = int(input())
  
  if(num == 0):
    stack.pop()
  else:
    stack.append(num)

for it in range(len(stack)):
  sum = sum + stack[it]
  
print(sum)
#콜라츠의 추측, 3n+1 문제, 우박수 문제라고 불리는 이 문제는 다음과 같다.
a, b = map(int, input().split())
maxKey = maxValue = 0

# def f1(n):
#     global cnt
#     cnt+=1
#     if(n == 1):
#         return cnt;
#     elif(n%2):
#         return f1(3 * n + 1);
#     else:
#         return f1(n // 2);

     
# for i in range(a, b+1):
#     cnt = 0;
#     cnt = f1(i);
#     if(cnt > maxValue):
#         maxKey = i
#         maxValue = cnt    
        
# print(maxKey,maxValue)


memo = { 1 : 1 }

def f2(n):
    global cnt
    cnt += 1
    if n == 1:
        return cnt
    
    if n in memo: 
        return f2(memo[n])
    
    elif(n%2):
        out  = 3 * n + 1
    else:
        out = n // 2;
    memo[n] = out
    return f2(out)

for i in range(a, b+1):
    cnt = 0
    f2(i)
    if(cnt > maxValue):
        maxKey = i
        maxValue = cnt    
    
print(maxKey,maxValue)
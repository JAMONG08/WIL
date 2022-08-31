#5! 구하기
def fac(n):
    if n == 1:
        return 1;
    return n * fac(n-1);
    
n = int(input())
print(fac(n))
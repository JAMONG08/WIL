# 등차수열 3n 123번째 나오는 수는?
# 시작값(a), 등차(d) 몇 번째인지 나타내는 정수(n) 출력함수 만들기 
start, diff, cnt = map(int, input('시작값 등차 몇번째 입력').split( ))

def dem(a, d, n):
    print( a + (n-1) * d )
    
dem(start, diff, cnt)

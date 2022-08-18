# 영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력
# ord(ch) : ch를 아스키코드의 숫자로 봔환
# chr(num) : num을 아스키코드의 문자로 반환 

char = int(ord(input()))
ch = int(ord('a'))

print(end='')

for ch in range(ch, char+1):
  print(chr(ch), end=' ')

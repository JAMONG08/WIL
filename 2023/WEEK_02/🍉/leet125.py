# https://leetcode.com/problems/valid-palindrome/

# 팰린드롬(palindrome) 앞 뒤로 똑같은 단어나 문장 
# 우영우 race a car
# A man, a plan, a canal: Panama
# 주어진 문자열이 팰린드롬인지 확인하기

# 시간 복잡도 O(N)
# 앞 뒤 하나씩 꺼내서 비교
import sys
from collections import deque

def isPalindrome(s: str) -> bool:
    #s = s.lower()
    
    str = deque()
    
    for char in s:
         if char.isalnum():
             str.append(char.lower())
        
    while len(str) > 1:
        if str.popleft() != str.pop():
            return False
        return True
    
input = sys.stdin.readline

print(isPalindrome(input()))

# 정규표현식 re 라이브러리 사용(리트코드는 내장) 
# 2배 시간 높일 수 있다 -> 파이썬의 문자열 슬라이싱은 짱 빠름

# def isPalindrome2(input):
#     input = input.lower()
#     input = re.sub('[^a-z0-9]','', input)
    
#     answer = (input == input[::-1])
#     return answer


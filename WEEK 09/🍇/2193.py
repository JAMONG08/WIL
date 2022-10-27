n = int(input())

d = [0, 1, 1]
for i in range(3, 91):
  d.append(d[i - 2] + d[i - 1])

print(d[n])


# 피보나치 수열 공식
# d = d[i-2] + d[i-1]

# 참고1 : https://m.blog.naver.com/occidere/220788046159

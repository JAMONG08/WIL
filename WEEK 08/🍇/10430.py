# (A+B)%C
# ((A%C) + (B%C))%C
# (A×B)%C
# ((A%C) × (B%C))%C

num = []

num = list(map(int, input().split(' ')))

A = num[0]
B = num[1]
C = num[2]

print((A + B) % C, end='\n')
print(((A % C) + (B % C)) % C, end='\n')
print((A * B) % C, end='\n')
print(((A % C) * (B % C)) % C, end='\n')

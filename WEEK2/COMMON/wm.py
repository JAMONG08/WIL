#정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

#방법1
n = int(input ('정수입력'))
total = 0

for i in range(1, n, 2):   
  total += i+1
  
print(total)

#방법2
max = int(input ('정수입력'))
n = max // 2
print(n * (n+1))

#============================
#C++
# #include<iostream>
# using namespace std;

# int add(int a)
# {
#     return a * (a+1);
# }

# int main() {
 
# int max, total = 0;
	
# 	cin >> max;	

# total = add(max/2);
 
#  cout << total;
# }
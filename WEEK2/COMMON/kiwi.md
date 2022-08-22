
### 문제
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.
##### 입력 예시
> 5
##### 출력 예시
> 6 (2 + 4)

### 문제 코드 구현
- Python
```python
n = int(input());
sum = 0;

for i in range(1, n+1):
  if(i%2 == 0):
    sum = sum + i

print(sum)
```

- java
```java
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); 
		
		int n = sc.nextInt();
		int sum = 0;
		for (int i = 1; i < n+1; i++ ) {
			if ( i % 2 == 0) {
				sum = sum + i;
			}		
		}
		System.out.println(sum);
	}
}
```

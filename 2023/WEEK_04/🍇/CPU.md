<<<<<<< HEAD
**CPU** : **''컴퓨터의 두뇌''** 메모리에 저장된 값을 <u>읽고, 해석하고, 실행함</u>
    ​			산술논리연산장치(**ALU** / 계산기), **레지스터**(**임시 저장장치**), **제어장치**(전기 신호로 명령어 해석) 으로 이루어짐
=======
**CPU** : **''컴퓨터의 두뇌''** 메모리에 저장된 값을 <u>읽고, 해석하고, 실행함</u><br>
    ​		산술논리연산장치(**ALU** / 계산기), **레지스터**(**임시 저장장치**), **제어장치**(전기 신호로 명령어 해석) 으로 이루어짐
>>>>>>> d3551bcedad277c10421584d9a36ffe797640643



1. **클럭** : 컴퓨터 부품들은 클럭 신호에 맞춰 움직임<br>
    a) 명령 사이클 : CPU는 명령 사이클의 흐름에 맞춰 명령어들을 실행함<br>
    b) 단위는 **헤르츠(Hz)** 1초에 클럭이 몇 번 반복되는지 나타냄(속도는 일정하지 않아서 순간 속도도 있음)<br>
    c) 클럭 속도만 높이면 <u>발열 문제</u> 생김

2. **코어** : **명령어를 실행**하는 부품 <br>
    a) CPU : 명령어 실행하는 부품 -> <u>명령어 실행하는 부품을 여러 개 포함하는 부품</u>(멀티코어. 멀티코어 프로세스)<br>
    b) 코어가 늘어나면 수행할 수 있는 명령어가 많아져서 <u>처리 속도 올라감</u>. But, 팀플레이 인원이 많다고 연산속도가 올라가는 건 아님 -> **명령어를 적절하게 분배하는게 연산속도가 달라짐**

3. **스레드** : 실행 흐름의 단위<br>
    a) **하드웨어적** 스레드 : <u>하나의 코어가 동시에 처리</u>하는 명령어 단위. <u>논리 프로세스</u><br>
    b) **소프트웨어적** 스레드 : <u>하나의 프로그램</u>에서 <u>독립적으로 실행</u>되는 단위

4. 멀티스레드 프로세스 : 레지스터 세트


<hr>

* **코어** : 명령어를 실행할 수 있는 ‘하드웨어 부품’<br>
* **스레드** : 명령어를 실행하는 단위 <br>
* **멀티코어 프로세스** : 명령어를 실행할 수 있는 하드웨어 부품이 CPU 안에 두개 이상 있는 CPU<br>
* **멀티스레드 프로세스** : 하나의 코어로 여러 개의 명령어를 동시에 실행할 수 있는 CPU

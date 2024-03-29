# 5-3 CISC와 RISC
'파이프라이닝 하기 쉬운 명령어'란?   
CPU의 언어인 ISA (Instruction Set Architecture)   
ISA를 기반으로 설계된 CISC, RISC   

## 명령어 집합
CPU가 이해할 수 있는 명령어들의 모음을 **명렁어 집합** 또는 **명령어 집합 구조(ISA)** 이라 부른다.   
CISC -> 인텔 -> x86-64   
RISC -> 애플 -> ARM

## CISC
**Complex** Instruction Set Computer   
x86, x86-64 대표적인 CISC 기반의 ISA입니다.   
**가변 길이 명령어**, **복잡**   
**프로그램을 실행하는 명령어가 작음**, **메모리 공간 절약**   
복잡함 -> 명령어 수행 시간이 길고 가지각색 (여러 클럭 주기 필요) -> 규격화 X -> 파이프라이닝 비효율   
대다수의 복잡한 명령어는 사용 빈도수가 낮음.    
```
즉, CISC 복잡하고 다양한 기능을 제공하기에 적은 수의 명령으로 프로그램을 동작시키고 메모리를 절약할 수 있으나
명령어의 규격화가 어려워 파이프라이닝이 어려움. 게다가 복잡한 명령어는 사용 빈도가 낮음.
```

## RISC
**Reduced** Instruction Set Computer   
ARM 대표적인 RISC 기반의 ISA입니다.   
CISC에 비해 명령어 종류가 적음.   
수행시간이 짧고(대부분 1클록 내외) 규격화 되어있음   
**고정 길이 명령어**   
레지스터를 적극 활용, 복잡 X -> 명령어를 많이 사용   

<hr>

옛날에는 RAM 메모리가 부족, CISC 기반에 인텔-x86이 인기가 많았고 유지되어왔음(독주체제)   
이후에는 메모리보다는 에너지 소비량(배터리)에 중심을 둠, 모바일 시대 덕분에 RISC ARM 각광받음.   
*프로세서 수행할 것이 복잡할 수록 에너지 소비가 많이 듬.   
*ARM 라이선스를 사서 맞춤형으로 변경함.(뼈대까지만 만들어서 설계 후 판매)   
CISC와 RISC 경계가 많이 사라짐.   
   

참고   
https://www.youtube.com/watch?v=G-fJJ-OHLDw   
https://www.youtube.com/watch?v=fBg-L6pwS_0   

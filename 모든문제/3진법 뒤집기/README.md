### 모든 문제 - 3진법 뒤집기
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3)

시간복잡도 : O(N) 

1. 주어진 n에서 str의 처음 index부터 n을 3으로 나눈 나머지를 str에 더한다. 이후 n을 3으로 나눈다.

2. 이렇게 되면 str에 3진수 역순으로 값이 저장되고, 이후 다시 str의 처음부터 answer에 3을 곱하고 str\[index\]값을 더한다.

___
### 참고
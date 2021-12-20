### 모든 문제 - 로또의 최고 순위와 최저 순위 
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/77484)

시간복잡도 : O(N^2)

1. 내가 가진 로또 번호 배열에서 0의 개수와, 정답 배열과 일치하는 수의 숫자를 계산한다.
2. 정답은 min(6,6-count-zeros+1) ~ min(6,6-count+1) 이다.
___
### 참고

1. list.count(value)를 통해 리스트에 있는 원소의 갯수를 간편히 구할 수 있다.
2. 순위를 저장하는 배열 rank = \[6,6,5,4,3,2,1\]을 통해 집계함수의 사용을 줄일 수 있다. (정답의 범위는 rank\[count+zeros\] ~ rank\[count\]이다.)
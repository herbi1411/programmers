### 모든 문제 - [1차] 추석 트래픽
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/17676?language=python3)

시간복잡도 : O(N)

1. lines 배열에서 각각 문자열을 etime, sec로 나눠서 각 task의 시작시간, 끝나는 시간을 새로운 배열 tasks에 저장한다. 이때 시작시간, 끝나는 시간은 ms단위의 Integer형으로 관리한다.
2. tasks배열을 작업의 시작시간 기준 오름차순으로 정렬한다.
3. 현재 진행중인 task를 나타낼 current 배열을 선언한다.
4. tasks배열의 각 원소마다 current 배열에서 작업시간이 초과된 원소(원소값+1000이 현재작업의 시작시간보다 작은 원소)를 제거한다.
5. answer의 값을 update한다. max(answer,len(current))
6. 현재 task를 current 배열에 추가한다. 이때 들어갈 값은 task의 etime이다.

___
### 참고

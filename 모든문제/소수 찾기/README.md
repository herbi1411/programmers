### 모든 문제 - 소수 찾기
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3)

시간복잡도 : O(NlogN) 
1. 나올 수 있는 모든 수를 저장할 집합을 만든다.
2. numbers에서 길이가 1~len(numbers)까지 나올 수 있는 모든 순열을 구한다.
3. 그 순열을 숫자로 변환하고 집합에 넣는다.
4. 집합의 원소 차례대로 소수인지 판별하고, 소수면 answer에 1 더한다.
___
### 참고
* set의 update 메서드
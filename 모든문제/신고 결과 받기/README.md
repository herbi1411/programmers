### 모든 문제 - 신고 결과 받기

___

[링크](https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3)

시간복잡도 : O(N)

1. 각 유저를 indexing하기 위해 dict를 선언 후 값을 순서대로 넣는다.

2. user \* user 크기의 2차원 배열을 만든다

3. report를 순회하며 2차원 배열의 신고당한 사람, 신고한 사람의 index의 값을 1로 한다.

4. 다시 2차원 배열을 순회하며 각 행마다 합이 k를 넘으면, 그 행에서 값이 1인 index를 찾아 answer배열의 같은 index값을 1로 만든다.


___
### 참고
* 2차원배열 선언의 얕은 복사 (행을 선언할 때는 for문을 써야함)
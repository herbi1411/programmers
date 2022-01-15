### 모든 문제 - 짝지어 제거하기
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/12973?language=python3)

시간복잡도 : O(N)

1. queue를 생성한다.
2. str의 각 문자를 반복문으로 돌면서 문자가 queue의 top과 같으면 해당 원소를 pop한다.
3. 해당 원소가 없으면 문자를 queue에 넣는다.
4. 이렇게 해서 문자열을 다 돌았을 때 queue가 비어있지 않으면 '짝 지어 제거하기'를 완성할 수 없다.
___
### 참고

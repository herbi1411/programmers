### 2019 카카오 개발자 겨울 인턴십 - 불량 사용자
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3)

시간복잡도 : O(N^2)

1. banned_id의 원소마다 올 수 있는 user_id를 저장할 banned_list 리스트를 만든다.
2. banned_id에서 원소를 하나씩 꺼내서 user_id의 원소들과 비교한 뒤에 넣을 수 있으면 banned_list에 추가한다.
3. banned_list에 추가된 user_id의 index들을 바탕으로 dfs를 돌며 가능한 user_id들의 집합을 구한다.
4. 집합의 중복여부는 dfs를 돌며서 리스트에 원소를 더하고 빼서, 최종 stage가 됐을 때 이미 추가된 결과 리스트와 원소들을 하나씩 비교하면서 중복되는 리스트가 없다면 해당 리스트를 결과 리스트에추가한다.

___
### 참고

1. 불량사용자가 나올 수 있는 조건을 잘 고려해야한다. 각각의 banned_id에 대해서 가능한 경우를 단순 곱하면 중복되는 경우가 생긴다.
2. user_id를 바로 DFS에 넣어 풀 수 있는 문제가 아니다. user_id 중에 하나라도 banned_id에 들어갈 수 없다면 함수가 종료된다.


___
### 다른사람 풀이

1. 처음에 user_id를 글자수에 따라 분류할 필요없이, banned_id를 기준으로 dfs를 돌린다.

2. visit배열에 체크를 하며 len만큼 dfs를 돌았을 때는 집합에 visit배열 정보를 넣는다.

3. 2의 방법을 통해 같은 id집합의 중복을 피할 수 있다.

[참고](https://imnotabear.tistory.com/422)
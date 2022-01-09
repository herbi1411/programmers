### 모든 문제 - 카카오 프렌즈 컬러링북
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/1829?language=cpp)

시간복잡도 : O(M*N)

1. 좌표에서 방문한 위치를 기록할 2차원 배열 visit을 선언한다.
2. 좌표의 (0,0)위치에서 부터 visit\[i\]\[j\]의 값이 0이고, picture\[i\]\[j\]의 값이 0이 아니면 해당 위치에서 DFS를 실행한다.
3. DFS는 해당 좌표에서 상하좌우 위치를 방문하며 해당 위치의 visit값이 0이고, picture의 값이 같으면 영역의 사이즈를 늘리며 해당 위치에서 다시 DFS를 진행한다. 
___
### 참고

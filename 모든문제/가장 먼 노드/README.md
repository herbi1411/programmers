### 모든 문제 - 가장 먼 노드 
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3)

시간복잡도 : O(N+M)

1. Djikstra 알고리즘을 이용해 PQ에 1번 Node부터 넣는다.
2. 이후 알고리즘에 따라 현재 노드의 간선을 보면서 연결된 노드들을 PQ에 추가한다.
___
### 참고

* BFS를 통하면 더 빠르게 구할 수 있다.
* Prim Algorithm을 써도 Djikstra보다 더 빠르다 (가중치가 모두 1이므로)
### 모든 문제 - 삼각 달팽이
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/68645?language=python3)

시간복잡도 : O(N^2)

1. 달팽이는 (왼쪽 대각선 아래, 오른쪽, 왼쪽 대각선 위) 의 순서로 순회한다.
2. 또 한 방향에서는 처음에 n개부터 1개씩 빼면서 채운다.
2. 두 규칙을 활용해 배열이 모두 채워질때까지 반복한다.

___
### 참고
* 2차원 배열에서 모든 원소들을 포함한 1차원 배열을 만들려면 sum(list,\[\])를 통해 만들 수 있다.
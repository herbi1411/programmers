### 모든 문제 - 등굣길
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/42898?language=python3)

시간복잡도 : O(M * N)

1. N * M 짜리 좌표를 만든다.
2. 좌표 (0,0)을 1로 설정한다.
3. 모든 좌표에대해 위쪽과 왼쪽에 있는 값을 더한다.
4. 이때 현재좌표가 물웅덩이라면 값을 0으로 바꾼다.

___
### 참고
* 실패코드 -> 물웅덩이의 좌표를 초기에 잘못설정했다.
    1. 주어진 좌표는 좌표가 1로 시작한다. 
    2. 첫열과 첫행을 1로 채울 때 물웅덩이를 만나면 멈춰야한다.
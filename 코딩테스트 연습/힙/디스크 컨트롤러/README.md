### 힙-2-디스크 컨트롤러
___

- 시간복잡도 = O(N^2) ? O(NlogN) ?

1. 리스트를 (요청시점 ASC,소요시간 ASC) 순서로 정렬한다

2. 작업의 갯수만큼 반복문을 돌며 현재시간보다 요청시점이 더 전인 원소들을 찾는다.

3. 원소들 중에 소요시간이 가장 적게 걸리는 작업을 현재 진행할 작업으로 선정한다.

4. 해당 작업의 소요시간을 현재 시간에 더하고, 정답에 (작업 후 현재시간 - 요청시간)을 더한다

5. 모든 작업이 종료 되고나서 평균을 구하기 위해 정답값을 작업의 갯수로 나눈다.



[링크](https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3)

___
### 다른 풀이
- 작업을 진행하고 다음 작업할 후보를 구하는 과정에서, 리스트를 새로 만들어서 최소값을 구하는 방법 말고, priority queue를 통해서 queue에 담고 pop해서  작업 시간이 가장 작은 작업을 구하는 방법도 있다.
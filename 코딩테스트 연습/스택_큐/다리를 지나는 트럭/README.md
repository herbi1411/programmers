### 스택/큐-3-다리를 지나는 트럭
___

- 시간복잡도 = O(N)


    1. 크기가 다리의 길이인 리스트를 만들어 원소를 0으로 채운다.

    2. 차례대로 다리의 0번 원소를 뺀 후에 트럭을 하나씩 다리에 넣는다. 이때 다리의 허용무게가 초과되면 트럭 대신에 0을 넣는다. 반복되는 횟수를 카운트한다.

    3. 모든 트럭이 다리에 들어갈 때 까지 2를 반복한다.

    4. 트럭이 모두 들어가면 총 반복된 횟수에 다리의 길이만큼을 더한 다음 값을 반환한다.

[링크](https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3)


___
### 다른 사람 풀이

- deque를 사용하면 더 효율적으로 문제를 풀 수 있다. (일반 리스트는 pop을 사용하면 모든 요소를 땡겨야한다)

- deque는 pop의 시간복잡도가 O(1)이지만 list는 O(N)이다.
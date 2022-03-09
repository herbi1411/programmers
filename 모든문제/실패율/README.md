### 모든 문제 - 실패율
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3)

시간복잡도 : O(NlogN) 

1. 주어진 stages에서 stage별로 머물고있는 유저의 수를 counter를 통해 count한다.

2. stages에서 각 stage의 내림차순으로 방문하면서 실패율을 각각 계산한다. (실패율을 담을 dict 선언 필요)

3. 내림차순으로 계산함으로써 stage를 1번만 순회해서 실패율을 계산할 수 있다. (성공한 user의 수를 차례로 더해갈 수 있기 때문에)

4. 이후 dict의 items 메서드를 통해 실패율(value)의 내림차순으로 key(stage 번호)를 가져온다.

5. 이 값을 answer배열에 담는다.
___
### 참고

* 실패코드는 시간복잡도가 O(N^2)이며, 스테이지에 도달한 유저가 없는 경우 (divide by zero 에러가 발생한다.)
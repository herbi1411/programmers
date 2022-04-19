### 모든 문제 - 다단계 칫솔 판매
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/77486?language=python3)

시간복잡도 : O(len(sell) * log(Employees))

1. root user + enroll 순서대로 dict에 저장한다. (key:이름, val:인덱스)
2. 이후 parent 배열을 employee의 수만큼 할당한다음 referral을 참고해서 모든 노드의 부모 관계를 parent배열에 저장한다.
3. 이후 seller와 amount에서 하나씩 가져오면서 자신의 몫인 90%를 answer에 더하고 이후 parent 배열을 참고해 부모에게 접근한뒤 나머지 10%를 할당한다.
4. root node까지 가거나, 부모에게 할당된 값이 0이 될때까지 반복한다. 

___
### 참고
* 실패 => Tree의 depth가 커지면 부모에게 할당된 돈이 0인데도 root node까지 가게되므로 시간초과가 발생한다.
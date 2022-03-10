### 모든 문제 - 가장 큰 수 (참고)
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3)

시간복잡도 : O(NlogN) 

1. numbers에서 길이가 다른 숫자또한 비교하기 위해 각 숫자에 3을 곱한다.

2. 이후 내림차순으로 정렬한다.

3. 숫자를 붙일 때는 각 숫자가 같은 숫자를 3번 반복한 것이므로 길이 / 3 만큼만 붙인다.

___
### 참고

* 실패한 코드는 permutations 사용으로 시간이 오래걸림(시간복잡도: O(N!))
* 실패한 2번째 코드는 각 숫자의 길이가 다를때 정렬이 제대로 안됨
* sort함수에 임의의 compare함수를 쓰려면 functools를 import하고 cmp_to_key method에 compare함수를 넣고 key로 할당하면 된다.
### 모든 문제 - 124 나라의 숫자
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3)

시간복잡도 : O(N)

1. 124숫자의 각 숫자 위치마다 오는 숫자는 (n-1) // (3 * num)) % 3 이라는 규칙이 존재한다.
2. 이때 num은 (자릿수의 위치 - 1)이고, n은 자릿수가 올라갈때마다 (3 ** (num+1))만큼 빼준다. 
___
### 참고

* string에서 arr.append('a')와 arr+= 'a'의 차이
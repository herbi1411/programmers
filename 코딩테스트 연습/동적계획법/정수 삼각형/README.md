### 동적계획법-정수삼각형

- 시간복잡도 = O(N)

    1. 리스트의 끝 원소를 row에 저장한다.

    2. 리스트의 끝 전 원소부터 거꾸로 리스트를 순회한다.

    3. temp리스트를 만들어서 temp\[index\] = 순회하는 리스트\[index\] + max(row\[index\],row\[index+1\])값을 차례로 저장한다.

    4. row 를 temp리스트로 치환한다.

    5. 다 돌고나면 원소가 1개인 row 리스트가 남는다

    6. 해당 값을 반환한다.


[링크](https://programmers.co.kr/learn/courses/30/lessons/43105?language=python3)
### 모든 문제 - 메뉴 리뉴얼

___

[링크](https://programmers.co.kr/learn/courses/30/lessons/72411?language=python3)

시간복잡도 : O(N^3)

1. orders에서 각 주문마다 알파벳 순서로 정렬시킨다.

2. 주어진 course 배열의 길이만큼 반복문을 실행한다. 

3. 주어진 course 배열에서 삽입할 조합의 원소 개수 N을 가져온 후에, orders의 각 order을 가져와 구성할 수있는 N개짜리 조합을 만든다.

4. 이후 뒤 index에 위치한 oder의 조합을 차례대로 구한 후에, 일치하는 조합이 있으면 그 조합을 dict에 삽입후 값을 1 증가시킨다. 이미 dict에 있는경우 값만 1 증가시킨다.

5. course 개수별 반복이 한번 종료될 때마다, dict에서 val이 최댓값을 가지는 key들(1개이상)을 answer에 삽입한다.

6. 이때 삽입할 때는 join()을 활용해 조합을 문자열로 바꿔서 삽입한다. 

7. 마지막에 완성된 answer 리스트를 알파벳 순서로 정렬한다.
___
### 참고
* Combinations
* dict대신에 Collections의 Counter를 쓰면 O(N^2)으로 가능
* Counter의 most_common 메서드
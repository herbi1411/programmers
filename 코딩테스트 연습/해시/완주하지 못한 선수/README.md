### 해시-1단계-완주하지못한선수
___

- 해시를 이용하면 O(N)에 해결 가능 (Counter 사용)
- 본 코드에서는 처음에 리스트 remove 연산을 통해 답을 도출했으나 시간복잡도가 O(N^2)이므로 효율성에서 실패
- 두번째로 리스트를 정렬 한 뒤, 앞에서부터 없는 단어를 찾아냄. 시간복잡도 => O(NlogN)

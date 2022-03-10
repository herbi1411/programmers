### 모든 문제 - 뉴스 클러스터링
___

[링크](https://programmers.co.kr/learn/courses/30/lessons/17677?language=python3)

시간복잡도 : O(N^2) 

1. 주어진 str 2개를 각각 두개의 문자로 짝지어서 새로운 문자열 배열을 만든다. 이때 두개의 문자중 하나라도 알파벳이 아니면 건너뛴다. 

2. 이렇게 생성된 2개의 문자열 배열을 Counter를 통해 갯수를 세주고 dict로 변환한다.

3. 생성된 1번째 dict의 각 key를 순회하며 key가 2번째 dict에도 있으면, intersection값에 min(dict1\[key\], dict2\[key\])값을 더해주고, union값에 max(dict1\[key\],dict2\[key\])값을 더해준다.

4. key가 dict2에 없으면 union에 dict1\[key\]값을 더해준다.

5. 이후 dict2의 각 key값을 순회하며 해당 key가 dict1에 없었으면 union값에 더해준다.

5. floor(intersection / union * 65536) 값을 반환한다. 이때 union이 0이라면 65536을 반환한다.
___
### 참고

* re를 통해서도 문자열이 알파벳으로 이루어져있는지 검사할 수 있다. re.findall(\[^a-zA-z\]+,str\[i:i+2\])
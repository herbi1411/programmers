#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
using namespace std;

void dfs(const int target, const int m, const int n, int i, int j, vector<vector<int>> picture, int& size, int* visit) {
	if (visit[n*i + j] != 0 || picture[i][j] != target)
		return;
	visit[n*i + j] = 1;
	size += 1;

	//printf("i: %d, j: %d, size: %d\n",i,j,size);

	if (i >0) {
		dfs(target, m, n, i - 1, j, picture, size, visit);
	}
	if (j >0) {
		dfs(target, m, n, i, j - 1, picture, size, visit);
	}
	if (i<m - 1) {
		dfs(target, m, n, i + 1, j, picture, size, visit);
	}
	if (j<n - 1) {
		dfs(target, m, n, i, j + 1, picture, size, visit);
	}
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
	int number_of_area = 0;
	int max_size_of_one_area = 0;

	int* visit = NULL;

	visit = (int*)malloc(sizeof(int)*m*n);
	memset(visit, 0, sizeof(int)*m*n);

	for (int i = 0; i<m; i++) {
		for (int j = 0; j<n; j++) {
			if (visit[i*n + j] == 0 && picture[i][j] != 0) {
				int size = 0;
				int target = picture[i][j];
				dfs(target, m, n, i, j, picture, size, visit);
				max_size_of_one_area = max(max_size_of_one_area, size);
				number_of_area += 1;
			}
		}
	}

	free(visit);

	vector<int> answer(2);
	answer[0] = number_of_area;
	answer[1] = max_size_of_one_area;
	return answer;
}
#include <string>
#include <vector>
#define TMAX 1e18
using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long a = 0;
    long long b = 1e18;
    long long mid = 0;
    long long number = 0;
    
    while(a<=b){
        mid = (a + b) / 2;
        number = 0;
        for(int v: times){
            number += mid / v;
        }
        if(number < n)
            a = mid + 1;
        else if (number >= n){
            if(mid <= b)
                answer = mid;
            b = mid - 1;
        }
    }
    return answer;
}
#include <string>
#include <vector>
#define TMAX 1e18
using namespace std;

long long solution(int n, vector<int> times) {
    long long answer = 0;
    long long number = 0;
    long long a = 0;
    long long b = TMAX;
    long long mid = 0;
    long long temp;
    while(1){
        mid = (a+b) / 2;
        number = 0;
        for(int v : times){
            number += mid / v;
        }
        // printf("%lld %lld %lld\n",a,b,number);
        if(number < n){
            a = mid + 1;
        }
        else if(number > n){
            b = mid - 1;    
        }
        else{
            answer = mid;
            break;
        }
    }
    // printf("%d\n",answer);
    while(1){
        int target = answer - 1;
        temp = 0;
        for(int v : times){
            temp += target / v;
        }
        if(temp == n)
            answer--;
        else
            break;
    }
    return answer;
}
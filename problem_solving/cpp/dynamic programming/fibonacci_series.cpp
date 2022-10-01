/*
    sample example of dp
    1. space complexity O(N)
    2. time complexity O(N)
*/

#include<bits/stdc++.h>
#define MAX_VAL 10000
using namespace std;

int dp[MAX_VAL];

int fib(int num){
    if(num <=1)
        return num;
    if(dp[num] !=-1)
        return dp[num];
    return dp[num]=fib(num - 1) + fib(num - 2);
}

int main()
{
    memset(dp, -1, sizeof(dp));
    int number;
    cout<<"Enter a Number"<<endl;
    cin>>number;
    if(number < MAX_VAL || number >= 0)
        cout<<number<<"th Fibonacci Value is = "<<fib(number)<<endl;
    else
        cout<<"overflow"<<endl;
}

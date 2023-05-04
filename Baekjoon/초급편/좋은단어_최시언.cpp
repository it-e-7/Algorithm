#include <bits/stdc++.h>
using namespace std;
int n;
string s;

int main(){
int cnt=0;
// 여기에 스택 선언 시, 아래 for문에서 돌때마다 스택안 값들이 남아있어서 에러가 난다  

cin >> n;
for(int i=0; i<n; i++){
cin >> s;
// 한번 돌때마다 새로 stk 를 선언, 새 스택을 가져온다  
stack<char> stk;

for(auto k : s){
if((stk.size())&&(stk.top()==k)){
stk.pop();
} else {
stk.push(k);
}
}
if(stk.size()==0){
cnt++;
}
}
cout << cnt << "\n";

return 0;
}

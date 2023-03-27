#include<bits/stdc++.h>
#pragma warning(disable:4996)
#pragma warning(disable:6031)
using namespace std;
typedef long long LL;
void fastIO() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}
bool is_prime(LL num) {
    if (num == 1)return false;
    for (LL i = 2; i * i <= num; i++)
        if (num % i == 0)return false;
    return true;
}
bool is_valid(LL num) {
    while (num > 0) {
        if (num % 10 == 3 || num % 10 == 4 || num % 10 == 7)
            return false;
        num /= 10;
    }
    return true;
}
LL reverse(LL num) {
    LL rev = 0;
    while (num > 0) {
        if (num % 10 == 6)
            rev = rev * 10 + 9;
        else if (num % 10 == 9)
            rev = rev * 10 + 6;
        else
            rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}
int main()
{
    fastIO();
    LL n;
    cin >> n;
    if (!is_prime(n))
        cout << "no" << '\n';
    else {
        if (!is_valid(n))
            cout << "no" << '\n';
        else {
            n = reverse(n);
            if (!is_prime(n))
                cout << "no" << '\n';
            else
                cout << "yes" << '\n';
        }
    }
    return 0;
}

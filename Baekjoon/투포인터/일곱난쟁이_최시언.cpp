//이거 그 소금물 문제 맞지..
//뒤집어서 총합을 구한 다음에 두개를 골라 빼면 좀 더 빠르지 않을까?

#include <stdio.h>
#include <iostream>
#include <algorithm> //sort떄문에 포함
#include <vector>
#include <numeric>

using namespace std;

int box;
int j, k;

int main(void) {
	vector<int> nine_guy;
	for (int i = 0; i < 9; i++){
		cin >> box;
		nine_guy.push_back(box);
	}
	sort(nine_guy.begin(), nine_guy.end()); //정렬 한 번 해줘야됨. 그래야 출력 편하지..

	/*do {
		cout << s << '\n';
	} while (std::next_permutation(s.begin(), s.end())); next_purmutation 공부하기!*/

	int sum = accumulate(nine_guy.begin(), nine_guy.end(), 0);
	for (j = 0; j < 9; j++) {
		for (k = j+1; k < 9; k++) {
			if (100==(sum - nine_guy[j] - nine_guy[k])) {
				goto END;
			}
		}
	}

	END:
	for (int l=0; l<9;l++){
		if( !((j==l)||(k==l)))
		cout << nine_guy[l] << '\n';
	}
}

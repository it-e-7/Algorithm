# [28075]스파이

"""
 민겸이가 전날에 임무를 수행한 곳과 같은 장소를 선택하면 그 날은 원래의 절반에 해당하는 진척도만 얻을 수 있다
 이때, 장소가 같다면 임무가 달라도 얻는 진척도는 원래의 절반이 됨

 기여도(M) = 진척도의 합

 M 이상의 기여도를 얻을 수 있는 임무 수행 방법이 몇 가지인지?

임무를 수행하는 총 일수 N
민겸이가 얻고 싶은 최소 기여도 M
info = 수족관, 시청, 학교
watch = 수족관, 시청, 학교
"""

N, M = map(int(input()))
info = []
watch = []
for i in range(N):

    list(map(int, input().split()))

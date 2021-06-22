'''

 Backjoon _ exampels #

  "Baek 14889 - 스타트와 링크"   by Jinwoo Lee


 # Algorithm 

  0. score 표를 참조하여 두 팀의 시너지 스코어 차이가 최소값을 출력하라.

  1. itertools 의 combinations을 사용하여 팀을 나눈다

  2. 두 팀에 대한 점수를 계산하여 result에 추가한다

  3. 최종적으로 min(result) 출력




 # Attention for Implementation

  - N/2 가 3이상일 경우 [1,3,5] 이라면 팀의 점수는 s_13, s_15, s_31, s_35, s_51,s_53  다 더하는 것으로 한다.

  - cal 함수에서 2중 포문 사용시 len이 아니고 team을 써야 됨


'''

from itertools import combinations

num_user = int(input())
users = [value for value in range(1,num_user+1)]
score = [list(map(int,input().split())) for _ in range(num_user)]
combination_users = list(combinations(users,num_user//2))


def cal(team, score):

    total = 0 
    for number in team:

        for cmp_number in team:

            total += score[number-1][cmp_number-1]

    return total



result = []

for com_user in combination_users:

    alpha = []
    beta = []
    alpha_total = 0
    beta_total = 0


    # seperate team
    for user in users:

        if user in com_user: alpha.append(user)
        else: beta.append(user)

    # cal scores
    alpha_total = cal(alpha,score)
    beta_total = cal(beta,score)

    result.append(abs(int(alpha_total - beta_total)))


print(min(result))


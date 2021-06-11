'''

 Backjoon _ exampels #

  "Baek - 2581 소수"

 by Jinwoo Lee ( 2021/06/11 )


 # Attention for Implementation

  - 1 (소수x) , 2(소수o)

  - 시간제한 문제일떄, 특정 범위( m < x <=n)의 모든 수에 대해 소수를 계산하면 시간초과 발생 

    => range(2, value)로 하여 한번이라도 나누어 떨어지는 부분이 있다면 break 하는 형태로 시간을 줄일 수 있음 



'''

m = int(input())
n = int(input())

answer = []

for value in range(m, n+1):

    cnt = 0
    # 1일 경우 처리 
    if value == 1:
        continue
    # 시간을 줄이기 위해 2~value까지 소수 계산 도중
    for chk_value in range(2, value):

        # 한번이라도 나누어떨어진다면 cnt+=1 하고 break -> 시간 감축
        if value % chk_value == 0:

            cnt +=1
            break

    if cnt == 0:
        answer.append(int(value))


if len(answer) ==0:
    print(-1)

else:
    print(sum(answer))
    print(min(answer))
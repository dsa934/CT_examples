'''

 Backjoon _ exampels #

  "Baek - 1018 체스판 다시 칠하기 "

 by Jinwoo Lee ( 2021/06/10 )


 # Attention for Implementation

  - chess 판나누기

  - 각 타일별 색깔 확인

    => 짝수좌표의 체스판이 B or White일 경우로 나누어서 풀면 된다 


    * 최초풀이시 첫타일을 기준으로 했기 떄문에 아래와 같은 반례에 대해 오류가 생김 

        * 반례 
        8 8
        BBWBWBWB
        BWBWBWBW            => 이경우 첫번쨰 타일 'B' -> 'W'로 바꿔주면 2번만에 끝남 
        WBWBWBWB
        BWBBBWBW
        WBWBWBWB
        BWBWBWBW
        WBWBWBWB
        BWBWBWBW

        답 : 2

'''

n, m = list(map(int,input().split()))

chess = []

for _ in range(n):

    chess.append(input())
result=[]

# cut chess
for row in range(n-7):

    for col in range(m-7):

        # check colors
        total = 0
        total2 = 0

        for row_idx in range(row,row+8):

            for col_idx in range(col,col+8):

                # 좌표합 짝수가 white인 경우
                if (row_idx + col_idx) %2 == 0 and chess[row_idx][col_idx] =='B':
                    total +=1

                if (row_idx + col_idx) %2 != 0 and chess[row_idx][col_idx] =='W':
                    total +=1

                # 좌표합 짝수가 black인 경우
                if (row_idx + col_idx) %2 == 0 and chess[row_idx][col_idx] =='W':
                    total2 +=1

                if (row_idx + col_idx) %2 != 0 and chess[row_idx][col_idx] =='B':
                    total2 +=1

        result.append(total)
        result.append(total2)


print(result)
print(min(result))

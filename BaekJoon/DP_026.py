
'''

 Backjoon _ exampels 1495

  "기타리스트 "   by Jinwoo Lee

  < algorithm >

  1. 냅색 알고리즘 사용 ( i번쨰 물건 포함, 미포함에 따른 값 비교가 필요한 경우 )

      n / m   0  1  2  3  4  5  6  7  8  9  10 ... m 
      
      start                  1
       
       3      1                              1

       5                1          1  

       7      1                               1
       


  2.  최초에 냅색을 생각했으며, dp_table 구성축 (raw: 노래 수, col :볼륨 )도 정혹하게 찾았으나, 

      dp_table[x][y] 에 들어가는 값을 수치적으로 더하고 뺴다보니 문제가 발생, 

      다음 기회에는 구하는 값과 축이 같은것을 이용하여 on / off( 1 or 0 )로 냅색 알고리즘 활용해보기 




  * 0 ~ n-1 

    => i번쨰 곡 시작전 볼륨을 조정 했을 때 (+- volume[i] ), M을 넘기지 않으면서, 마지막 곡을 연주할떄의 볼륨 크기를 구하는 것

    => m을 구하는것이 아님 (혼동 x)

    => 곡이 n개면, 볼륨 조절은 n-1번만 하기 떄문에,  n-1 번 반복해야할것 같지만, 시작부분에 해당하는 start를 포함하기 떄문에 n 번 진행해야 한다 

       따라서 for idx in range(1, n+1) 이 아닌,  for idx in range(n) 이 되는 것 

 

'''

def solution():

    n, s, m = list(map(int, input().split()))

    volume = list(map(int, input().split()))

    dp_table = [ [0 for _ in range(m+1) ] for _ in range(n+1) ]


    dp_table[0][s]= 1


    for idx in range(n):

        for cmp_idx in range(m+1):

            if dp_table[idx][cmp_idx] == 1:

                if cmp_idx + volume[idx] <= m :

                    dp_table[idx+1][cmp_idx + volume[idx] ] = 1

                if cmp_idx - volume[idx] >= 0 :

                    dp_table[idx+1][cmp_idx - volume[idx] ] = 1

    result = -1 

    for idx in range(m,-1,-1):
        
        if dp_table[n][idx] == 1 :

            result = idx
            break


    print(result)

solution()
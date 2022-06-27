


'''

 Backjoon _ exampels 2407

  "조합"   by Jinwoo Lee

  < algorithm >

  1. 조합을 구하는 문제는 파스칼의 삼각형을 생각하기

  2. 파스칼의 삼각형 init value =>   [0][0] , [1][0], [1][1] = 1 ,1 ,1  로 셋팅 

  * but, n>= 1000 이상의 큰 제한일 경우, 파스칼의 삼각형으로 조합을 구하는건 TLE가 걸림 

    떄문에 페르마의 소정리 , 뤼카의 정리 등으로 더 빠르게 구할 수 있는데

    이는 gold level인듯 함  => 추후 이부분에 대해 정리해야 함 (2022-06-27)


 
    ref. https://rebro.kr/107

'''






def solution():

    n, m = map(int , input().split())
    

    dp_table = [ [0 for _ in range(n+1)] for _ in range(n+1) ]
    
    dp_table[0][0], dp_table[1][0] , dp_table[1][1] = 1, 1, 1
    

    for row_idx in range(2, n+1):
        
        for col_idx in range(0, row_idx+1):
            

            if col_idx == 0 : 
                
                dp_table[row_idx][col_idx] = dp_table[row_idx-1][col_idx]
                
            else:
                
                dp_table[row_idx][col_idx] = dp_table[row_idx-1][col_idx] + dp_table[row_idx-1][col_idx-1]
                

    print(dp_table[n][m])
    
solution()
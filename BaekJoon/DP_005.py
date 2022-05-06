

'''

 Backjoon _ exampels 1149

  "RGB Distance"   by Jinwoo Lee

  < algorithm >

  1. F[current_floor, color]  += min ( F(prev_floor, other_color) + F(prev_floor, other_color) ) 


  2. DP로 풀어야 하는 이유 

    15 13 15       =>  greedy로 풀 경우, 1층에서 최소비용인 Green(13)을 선택하고, 2층에서는 red or blue을 선택하여 cost = 23 
    10 1  10         
                       but, 2층의 최소비용이 Green(1) 임으로 greedy가 최적해를 보장하지 못한다. 

                       따라서 현재 칸 (t)에서 이전칸(t-1)을 고려하는 방식으로 층수를 dp_Table에 쌓아가며 진행하면 된다.


  3. <초기값 설정 >  

     * [floor, red] 를 키값으로 각각에 해당하는 cost를 초기값으로 설정 


  4. 1에서 정의한 <관계식>을 코드로 풀이 



 

'''

def rgb_distance():

    num_house = int(input())

    info_house = [ list(map(int, input().split())) for _ in range(num_house)]


    # 0: red, 1: green, 2: blue
    for floor in range(1, num_house):
        
        info_house[floor][0] += min( info_house[floor-1][1], info_house[floor-1][2])
        info_house[floor][1] += min( info_house[floor-1][0], info_house[floor-1][2])
        info_house[floor][2] += min( info_house[floor-1][0], info_house[floor-1][1])
        
    return min(info_house[-1])

print(rgb_distance())

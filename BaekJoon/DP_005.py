

'''

 Backjoon _ exampels 1149

  "RGB Distance"   by Jinwoo Lee

  < algorithm >

  1. F[current_floor, color]  += min ( F(prev_floor, other_color) + F(prev_floor, other_color) ) 


  2. DP�� Ǯ��� �ϴ� ���� 

    15 13 15       =>  greedy�� Ǯ ���, 1������ �ּҺ���� Green(13)�� �����ϰ�, 2�������� red or blue�� �����Ͽ� cost = 23 
    10 1  10         
                       but, 2���� �ּҺ���� Green(1) ������ greedy�� �����ظ� �������� ���Ѵ�. 

                       ���� ���� ĭ (t)���� ����ĭ(t-1)�� ����ϴ� ������� ������ dp_Table�� �׾ư��� �����ϸ� �ȴ�.


  3. <�ʱⰪ ���� >  

     * [floor, red] �� Ű������ ������ �ش��ϴ� cost�� �ʱⰪ���� ���� 


  4. 1���� ������ <�����>�� �ڵ�� Ǯ�� 



 

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

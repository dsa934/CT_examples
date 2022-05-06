
'''

 Backjoon _ exampels 9461

  " 파도반 수열"   by Jinwoo Lee

  < algorithm >
 
   1. F(n) = F(n-2) + F(n-3)   < 관계식 찾기 >

   2. init value = [1,1,1]     < 초기값 설정 >

   * 결국 dp 문제는 '관계식 찾기'를 통해 아래의 '3가지'를 만족하는지 체크하기 

     a) 해당 문제가 sub_problem으로 분할 되는지

     b) sub_problem의 해가 또 부모 문제를 풀때 사용 되는지

     c) sub_problem의 해가 다른 sub_problem에서 사용 되는지 ( Momoization )


   * 초기값 설정 (init value)을 통해 Top_down 방식이 아닌, ' Bottom_up ' 방식을 구현 



'''

def padoban():

    
    num = int(input())

    dp_table = [1,1,1]

    if num > len(dp_table):

        for idx in range(3,num+1):

            value = dp_table[idx-2] + dp_table[idx-3]

            dp_table.append(value)


    return dp_table[num-1]



num_test = int(input())

for _ in range(num_test):

    print( padoban() )
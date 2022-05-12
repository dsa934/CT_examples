
'''

 Backjoon _ exampels 11722

  "가장 큰 감소하는 수열 "   by Jinwoo Lee


  < algorithm >

  1. LIS 문제의 알고리즘 적용 but number list를 뒤집어서 수행 

   * 증가하는 수열의 반대라고 해서, info[idx] < info[cmp_idx]로 하게 되면,

     idx 기준, 최대 길이가 저장되는 것이 아니라 수열 중 가장 낮은 값을 가진 value의 dp[idx]에 저장되게 됨


   * 수열이 저장된 number list 자체를 뒤집어서 하면, 현 idx 기준, 감소하는 수열의 길이를 저장할 수 있음 


 

'''


def solution():

    num = int(input())

    field = list(map(int, input().split()))

    dp = [ 1 for _ in range(num) ]

    rev_field=field[::-1]

    for idx in range(num):

        for cmp_idx in range(idx):

            if rev_field[idx] > rev_field[cmp_idx]:

                dp[idx] = max(dp[idx], dp[cmp_idx] +1)

    return max(dp)

print( solution() )



'''

 Backjoon _ exampels #

  "Baek - 1120 문자열(문자열)"   by Jinwoo Lee


 # Algorithm 

  0. 두개의 문자열 A,B에 대하여 len(A) <= len(b) 일때, A에 앞,뒤에 아무 알파벳을 추가하여 길이를 맞출 수 있다 이때 A,B의 차가 최소가 되도록 하는 프로그램 

  1. 두 문자열의 차이가 최소가 되어야 함으로, 추가되는 알파벳은 문자열 B에 있는 알파벳과 동일한 것을 추가 해야함으로 고려하지 않아도 된다.

  2. 따라서 주어진 문자열 A,B를 비교하면 되는데, A를 B의 어느 위치부터 비교할것인지에 따라 두 문자열의 차이가 다르게 된다 

  3. 2에서 구해지는 차이의 최소값을 출력 



 # Attention for Implementation

  1. differ의 범위 체크 



'''

string_a, string_b = list(input().split())


differ = len(string_b) -len(string_a)

result = [] 

# len(string_b) = 4, len(string_a) = 3일 경우 
# 비교시작위치는 string_b의 idx =0, 1 2개임으로 differ+1 사용 
for idx in range(differ+1):

    cnt = 0

    for cmp_idx in range(len(string_a)):

        if string_a[cmp_idx] != string_b[idx+cmp_idx] : cnt+=1

    result.append(cnt)

print(min(result))





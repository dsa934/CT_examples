
'''

 Backjoon _ exampels 1251

  "단어 나누기"   by Jinwoo Lee

  < algorithm >

  1. BF (Brute Force) 문제 

     => 단어를 끊어냄에 있어 어떠한 규칙을 찾을 수 없었음

     => 단어를 3개로 쪼개야 함으로 2번만 끊어내면 되기 떄문에 2중 포문 사용


     * first idx 
     
        * string range : 3 ~ 50 

        frist = string[:first_idx]  첫단어 형성 시 first_idx 가 0이면 빈칸이 됨으로 1부터 시작 

        string 의 길이가 3인 경우, 최소 3개의 단어로 쪼개져야 하기 떄문에 len(string)-2 까지만 따져야 한다

        ∴ for idx in range(1, len(string)-2) ) 


    * second idx

      for idx in range( first_cut +1 , len(string) )

      두번쨰 cut_idx의 범위 :  first_cut+1 ~ len(string) 인 이유는 아래와 같다.

      first = string[:i]      # i 미포함
      second = string[i:j]    # i 포함, j 미포함
      third = string[j:]      # j 포함


     
'''


def solution():

    string = list(input())

    answer = []

    for i in range(1,len(string)-2):

        for j in range(i+1, len(string)):


            first = string[:i][::-1]
            second = string[i:j][::-1]
            third = string[j:][::-1]
            
            answer.append("".join(first+second+third))


    print(sorted(answer)[0])
    

solution()
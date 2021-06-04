'''

 Programmers _ exampels #

  "큰수 만들기"

   by Jinwoo Lee ( 2021/06/04 )


 # Problem

  -   "1924"        => "94"
      "1231234"     => "3234"
      "4177252841"  => "775841"


 # Attention for Implementation

  - 삭제연산에 stack & while 활용해보기

  - 4177252841 에서 77 이후 2,5를 판단할때 2를지우고 5를 채워야하는 부분이 문제 였음

    => 일단 stack에 쌓고 value 값이 stack[-1]보다 큰 경우 해당되는 stack 안의 모든 원소를 제거하기 위해 while을 사용


'''


def solution(number, k):
    
    save = []

    for value in number:

        # save : not empty & save[-1] < value  & k > 0
        while save and save[-1] < value and k > 0 :

            k -= 1
            save.pop()

        save.append(value)

    # 마지막 save [ : len(save) -k ] 처리는 
    # 9999와 같이 중복된 수가 들어왔을 때 자리수를 처리해주기 위함
    print(''.join(save[:len(save)-k]))






solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)
solution("99999", 2)

#solution("6344177252841", 4)

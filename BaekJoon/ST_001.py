
'''

 Backjoon _ exampels 1251

  "�ܾ� ������"   by Jinwoo Lee

  < algorithm >

  1. BF (Brute Force) ���� 

     => �ܾ ����� �־� ��� ��Ģ�� ã�� �� ������

     => �ܾ 3���� �ɰ��� ������ 2���� ����� �Ǳ� ������ 2�� ���� ���


     * first idx 
     
        * string range : 3 ~ 50 

        frist = string[:first_idx]  ù�ܾ� ���� �� first_idx �� 0�̸� ��ĭ�� ������ 1���� ���� 

        string �� ���̰� 3�� ���, �ּ� 3���� �ܾ�� �ɰ����� �ϱ� ������ len(string)-2 ������ ������ �Ѵ�

        �� for idx in range(1, len(string)-2) ) 


    * second idx

      for idx in range( first_cut +1 , len(string) )

      �ι��� cut_idx�� ���� :  first_cut+1 ~ len(string) �� ������ �Ʒ��� ����.

      first = string[:i]      # i ������
      second = string[i:j]    # i ����, j ������
      third = string[j:]      # j ����


     
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
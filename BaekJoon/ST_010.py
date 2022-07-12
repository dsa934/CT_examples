

'''

 Backjoon _ exampels 4821

  "������ ����"   by Jinwoo Lee

  < algorithm >

  1. Ư�� ���� '-' , ' ' �� ���Ͽ� �Է¹��� ���ڿ��� split()�� ���� �ι� �и�

  2. �������� �ߺ� �Ǹ� �ȵǱ� ������ set() �ڷ� ������ ����Ͽ�  ���� �� ������ �߰�

  3. ���� ���� chk 

    1) start > num 

    2) end > num && start < num �̸�, start ~ num ���� 

    3) end < start


  * ���� �õ� - AC ���� ����

    => �и��� ���ڿ��� (start,end) �� ���� ���°� �ƴ�, (just_one_page) 1���� ��쿡,

       just_one_page > num �� ��� �μ⸦ �� �� ���� ������ ���� 

       num : ������ �� ������ �� ��� �������� ���� 

       => num�� '�μ��ؾ� �� ���� ��ġ ���� ����' �� �ƴ϶� '�μ� ������ �������� ����' �� �ǹ� �� 

 

'''



def solution():

    while True:

        num = int(input())

        if num == 0 :break

        candidate = set()

        string = input().split(",")

        sub_string = [ value.split("-") for value in string ]


        for value in sub_string:

        
            if len(value) == 1: 
                
                if int(value[0]) > num : continue
                else:
                    candidate.add(int(value[0]))

            else:

                s, e = value
                s, e = int(s), int(e)

                if e < s : continue

                elif num < s : continue  

                else:

                    for value in range(s,e+1):

                        if value > num : break

                        else:
                            candidate.add(value)

                            
        print(len(candidate))

solution()
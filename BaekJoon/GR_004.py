
'''

 Backjoon _ exampels 21313

  "����"   by Jinwoo Lee

  < algorithm >

  1. if even number then answer = [1,2] * (num//2)

  2. if odd number then answer = [1,2] * (num//2) + [3]


  �� answer = [1,2] * (num//2) + ( [3] if num%2 else [] )

    => if <���ǹ�> ���� ���ǹ� �κ��� 0�̸� False, �� �� �ٸ� ���ڸ� True

    => ( [3] if num%2 else []  ) ���� () �� �����ϸ� ��� ������ ���� ����

       ��Ȯ�� ������ ���� ��������, () �����ϸ� [1,2] * (num//2) + [3] ���Ŀ� if ������ �Ǵ��� ���� ���� �� ����




  * �׸��� ���ؼ� 1���� N���� ������ ������ 2��� �Ѵٰ� �߸� �����ؼ� Ʋ�ȴ� ����

    => �׸��� ��Ȥ ���� ���� ���� ������ ���� �� �����ϰ� �б�


 '''   
 



    
def solution():
    
    num = int(input())

    answer= [1, 2] * (num//2) +([3] if num %2  else [] )

    print(answer)
    
solution()
     

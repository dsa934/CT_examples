'''

 Programmers _ exampels 7

  "최대공략수 & 최소공배수"

 by Jinwoo Lee ( 2021/05/27 )


 # Problem

  - 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
  - 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.


 # Attention for implementation

  - 문제 자체는 쉽지만, 교집합을 사용할때 정렬을 해주지 않으면 생각한것과 다르게 순서가 이상하게 정렬 될 수 있음에 유의 
 

'''
def solution(n, m):
    
    # set init params
    n_divisor = []
    m_divisor = []
    result = []
    
    for n_value in range(1,n+1):
        
        if n % n_value == 0:
            
          n_divisor.append(n_value)
        
    for m_value in range(1,m+1):
        
        if m % m_value == 0:
            
          m_divisor.append(m_value)
          
    common = sorted(list(set(n_divisor) & set(m_divisor)))
    
    if len(common) == 1:
        result.append([common[0], n*m ])
        
    else:
        result.append([common[-1], int(common[-1] * n/common[-1] * m/common[-1])])
    
    return result[0]

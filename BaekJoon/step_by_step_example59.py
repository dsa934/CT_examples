'''

 Backjoon _ exampels #

  "Baek 15250 - ACM호텔 (구현)"   by Jinwoo Lee


 # Attention for Implementation


'''

num_test = int(input())

info = [list(map(int,input().split())) for _ in range(num_test)]

result = []

for idx in range(num_test):

    h,w,n = info[idx]

    moc = (n // h ) +1

    namage = n % h 

    if namage == 0 : 

        moc = n//h
        namage = h
        
    if moc < 10 : result.append(''.join(str(namage) + str(0)+str(moc)))
    else : result.append(''.join(str(namage)+str(moc)))
    
for value in result:
    print(value)
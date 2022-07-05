


'''

 Backjoon _ exampels 4378

  "트ㅏㅊ;"   by Jinwoo Lee

  < algorithm >

  * 특수문자의 경우 \\ , \' 와 같이 선언 해야 함

     ' 의 경우 " " 로 감싸면 \ 사용하지 않아도 된다

     \ 의 경우 \\로 표현해야 제대로 표현 됨


  * 입력이 여러줄이며, 각 줄마다 오류를 고쳐서 출력해야 함으로 try ~ except 구문 사용 

 
  * 최초 시도에서 keyboard dict 구현 시 무엇인가 뺴먹은것이 있는것 같다.

'''


def solution():

    keyboard = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "W": "Q", "E": "W", "R": "E", "T": "R", "Y": "T", "U": "Y", "I": "U", "O": "I", "P": "O", "[": "P", "]": "[", "\\": "]",
        "S": "A", "D": "S", "F": "D", "G": "F", "H": "G", "J": "H", "K": "J", "L": "K", ";": "L", "'": ";",
        "X": "Z", "C": "X", "V": "C", "B": "V", "N": "B", "M": "N", ",": "M", ".":",", "/": ".", " ": " "
    }

    while True:


        try:
            answer = [] 

            sentence = input()
            
            for value in sentence:
                
                answer.append(keyboard[value])
            

            print(''.join(answer))

        except :
            break



solution()




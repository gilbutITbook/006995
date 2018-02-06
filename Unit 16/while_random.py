import random    # random 모듈을 가져옴

i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(0, 9)    # randint를 사용하여 0부터 9까지 무작위로 정수를 생성
    print(i)
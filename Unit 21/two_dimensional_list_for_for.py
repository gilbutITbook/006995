a = [[10, 20], [30, 40], [50, 60]]

for i in a:        # a에서 안쪽 리스트를 꺼냄
    for j in i:    # 안쪽 리스트에서 값을 하나씩 꺼냄
        print(j, end=' ')
    print()
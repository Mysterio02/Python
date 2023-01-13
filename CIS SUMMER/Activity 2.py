


i = 0
while i < 3:
    print(i)    # 0, 1, 2
    i += 1
    
    
for i in range(3):
    print(i)    # 0, 1, 2
    
    
for i in range(0, 10, 2):
    print(i)    # 0, 2, 4, 6, 8
    
    
i = 0
while True:
    print(i)    # 0, 1, 2
    i += 1
    if i >= 3:
        break
    
    
for i in range(10):
    if i % 2:
        continue
    print(i)    # 0, 2, 4, 6, 8
    
    
for i in range(1, 4):
    for j in range(1, 4):
        print(str(i) + str(j), end = '\t')
    print()
print()

i = 1
while i < 4:
    j = 1
    while j < 4:
        print(str(i) + str(j), end = '\t')
        j += 1
    print()
    i += 1
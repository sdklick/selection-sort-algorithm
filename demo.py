#selection sort implementation

data = [4, 1, 2, 5, 3]
size = len(data)

for x in range(size):
    for y in range(x+1, size):
        if data[x]>data[y]:
            data[x],data[y]=data[y],data[x]
         

print(data)
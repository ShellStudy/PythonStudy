f = open('app01\\data1.csv', mode='r', encoding='UTF-8')

arr = f.readlines()

for i in range(1, len(arr)):
    row = arr[i].replace("\n", "")
    arr2 = row.split(",")
    print(f'{int(arr2[1])} * {int(arr2[2])} = {int(arr2[1]) * int(arr2[2])}')

f.close()
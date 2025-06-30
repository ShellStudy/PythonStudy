print("안녕하세요")

file = open('app01\\text.txt', encoding='UTF-8', mode='w')
file.write('안녕하세요')

file.close()
file = open('app01\\text.txt', encoding='UTF-8', mode='r')
print(file.readlines())
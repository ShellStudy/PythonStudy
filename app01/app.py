print("안녕하세요")

file = open('app01\\text.txt', encoding='UTF-8', mode='w')
file.write('안녕하세요\n')
file.close()

file = open('app01\\text.txt', encoding='UTF-8', mode='r')
print(file.readlines())
file.close()

file = open('app01\\text.txt', encoding='UTF-8', mode='a')
file.write('추가 내용\n')
file.close()

file = open('app01\\text.txt', encoding='UTF-8', mode='r')
print(file.readlines())
file.close()
파일명 = input("신규 파일명을 입력하세요.")

신규파일 = open(f'app01\\{파일명}', mode='w', encoding='UTF-8')
글 = input("내용을 입력하세요.")
신규파일.write(글)

신규파일.close()
filename = input('введите имя файла(.txt): ')
text = input('Ваедите текст: ')
file = open(filename, 'w')
file.write(text)
file.close()
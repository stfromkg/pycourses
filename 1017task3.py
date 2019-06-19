filename1 = input('название 1го файла.txt: ')
filename2 = input('название 2го файла.txt: ')

file1 = open(filename1, 'r')
file2 = open(filename2, 'w')



file2.write(file1.read())

file1.close()
file2.close()




#file1 = open('C:/Users/Tokyo/PycharmProjects/true.txt', 'r',  encoding='utf-8')
#file2 = open('C:/Users/Tokyo/PycharmProjects/Fake.txt', 'w',  encoding='utf-8')
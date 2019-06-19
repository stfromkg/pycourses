import random
a = '1 3 4 5 6 7 8 9'
b = a.split()
print(b)
random.shuffle(b)
print(b)

f = open('C:/Users/Tokyo/Desktop/file2.txt', 'a', encoding='utf-8')
f.write(str(b))
f.close()
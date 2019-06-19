

f = open('C:/Users/Tokyo/Desktop/1file.txt', 'w', encoding='utf-8')
a = f.write("Superman is dead.RIP")
print(a)
f.close()


f = open('C:/Users/Tokyo/Desktop/2file.txt', 'r', encoding='utf-8')
a = f.read()
b = a.split()
print(b)
f.close()
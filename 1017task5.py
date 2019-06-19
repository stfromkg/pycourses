import re
a = {id:2;name:"Nastya";age:20;sex:"female"}   #обработать строку с помощью regular expressions и вывести все значения

b = re.findall(r'\D+:(\w)+;'a)
print(b)



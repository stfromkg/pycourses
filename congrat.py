def congrat(name, age):
   print("Поздравляю, " + name + " вам " + age +  " лет и вы проходите углубленный курс питон")
name = str(input())
age = str(input()) # почему не получается использовать int вместо str?
print(congrat(name, age))

a = int(input("num a :"))
b = int(input("num b :"))
print((a + 4*b)*(a - 3*b) + a**2)

#(a + 4b)(a-3b) + a**2

print("_______________")

def itog (a, b):
    return ((a + 4*b)*(a - 3*b) + a**2)
a = int(input())
b = int(input()) # не получается обьеденить a и b в одну строку((
print(itog(a, b))
'''
print("hello, djangogirls")
imie = "Marta"
print ("imie")
a = 3
b = 4
c = 5
a*b*c
print(a*b*c)
liczby = [1, 2, 3, 4]
print("liczby")
if 2>3:
    print("To działa!")
else:
    print("naprawdę?")
name = "Marta"
if name == "Marta":
    print("hej Marta")
elif name == "Ola":
    print("hej Ola")
else:
    print("Co tu robisz?")
'''

name = "Marta"

def hi():
    print("Hej!")
    print("Jak się masz?")
hi()
def hi(name):
    if name == "Marta":
       print("hej Marta!")
    elif name == "Ola":
        print("hej Ola")
    else:
        print("hej anonimie")
hi(name)
hi("Ola")
hi("Asia")
def hi(name):
    print("hej " + name + "!")
hi("Zuzia")
dziewczyny = ["Marta", "Ola", "Asia", "Mania"]
for imie in dziewczyny:
    hi(imie)
    print("Witaj" + name + "!")
for i in range(1, 6):
    print(i)






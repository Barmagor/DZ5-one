import random
def input1():
    a=0
    while a<1 or a>28:
        print("Введите число от 1 до 28")
        print("Сколько вы хотите взять конфет?")
        try:
            a=int(input())
        except ValueError:
            print("Введите корректное число")
    return(a)

var=random.randint(1, 2)
if var == 1:
    print("Игрок 1 ходит первым")
    var2=2
if var == 2:
    print("Игрок 2 ходит первым")
    var2=1
c=30
count=1
while 0<c:
    if count%2!=0:
        print(f"Игрок {var} ходит")
        if c>=28:
            b=input1()
            c=c-b
            player=var
        elif c<28:
            print("Сколько вы хотите взять конфет?")
            b=int(input())
            while b<1 or b>c:
                print("Осталось меньше конфет")
                print(c)
                print("Сколько вы хотите взять конфет?")
                b=int(input())
            c=c-b
            player=var
    elif count%2==0:
        print(f"Игрок {var2} ходит")
        if c>=28:
            b=input1()
            c=c-b
            player=var2
        elif c<28:
            print("Сколько вы хотите взять конфет?")
            b=int(input())
            while b<1 or b>c:
                print("Осталось меньше конфет")
                print(c)
                print("Сколько вы хотите взять конфет?")
                b=int(input())
            c=c-b
            player=var2
    count+=1
    if count > 2:
        count=1
if player == var:
    print(f"Победил игрок № {var}")
if player == var2:
    print(f"Победил игрок № {var2}")
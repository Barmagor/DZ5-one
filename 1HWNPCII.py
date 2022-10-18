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
    a=29
if var == 2:
    print("Игрок 2 ходит первым")
    var2=1
    a=28
print("Игрок 1 это ты!")
c=60
count=1
true_count=1
while 0<c:
    if count%2!=0:
        print(f"Игрок {var} ходит")
        if var==1:
            if c>=28:
                b=input1()
                c=c-b
                player=0
            elif c<28:
                print("Сколько вы хотите взять конфет?")
                b=int(input())
                while b<1 or b>c:
                    print("Осталось меньше конфет")
                    print("Сколько вы хотите взять конфет?")
                    print(c)
                    b=int(input())
                c=c-b
                player=0
        elif var==2:
            if c>=28:
                n=0
                while n<true_count:
                    a = a-2
                    n+=1
                c=c-a
                player=1
            elif c<28:
                c=0
                player=1
    elif count%2==0:
        print(f"Игрок {var2} ходит")
        if var2==1:
            if c>=28:
                b=input1()
                c=c-b
                player=0
            elif c<28:
                print("Сколько вы хотите взять конфет?")
                b=int(input())
                while b<1 or b>c:
                    print("Осталось меньше конфет")
                    print("Сколько вы хотите взять конфет?")
                    print(c)
                    b=int(input())
                c=c-b
                player=0
        elif var2==2:
            if c>=28:
                n=0
                while n<true_count:
                    a = a-2
                    n+=1
                c=c-a
                player=1
            elif c<28:
                c=0
                player=1
    count+=1
    true_count+=1
    if count > 2:
        count=1
if player == 0:
    print("Победил игрок № 1")
if player == 1:
    print("Победил игрок № 2")
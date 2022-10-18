def decode(my_string):
    decoded = ""
    i = 0
    j = 0
    while (i <= len(my_string) - 1):
        count = int(my_string[i])
        word = my_string[i + 1]
        for j in range(count):
            decoded = decoded+word
        i = i + 2
    return decoded 
        
a=open("fileB.txt", "r", encoding="UTF-8")
x=a.readlines()
print(x) 
num = decode(x[0]) 
print(num)
rec=open("file5.txt", "w", encoding="UTF-8")
rec.write(num)
rec.close()
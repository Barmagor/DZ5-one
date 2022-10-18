def encode_string(my_string):
    encode= ""
    i = 0
    while (i <= len(my_string)-1):
        count = 1
        element = my_string[i]
        j = i
        while (j < len(my_string)-1):   
            if (my_string[j] == my_string[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encode = encode + str(count) + element
        i = j + 1
    return encode
        
a=open("fileA.txt", "r", encoding="UTF-8")
x=a.readlines()
print(x)
num = encode_string(x[0]) 
print(num)
rec=open("file4.txt", "w", encoding="UTF-8")
rec.write(num)
rec.close()


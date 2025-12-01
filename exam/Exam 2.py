ASCII=[]

ASCII=str(input("sasir votre mots "))
ascii_value = [ord(char) for char in ASCII]

sous = [abs(ascii_value[i+1] - ascii_value[i]) for i in range(len(ascii_value)-1)]
total=sum(sous)
print(total)
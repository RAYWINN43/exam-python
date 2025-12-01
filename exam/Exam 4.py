numbers=[]
input_len = int(input("sasir le nombre de chiffre voulu TABLEAU "))

for i in range(input_len):
    val=float(input(f"entre vos chiffre { i + 1 } ;"))
    numbers.append(val)

numbers.sort()

dernier_chiffre = numbers[-1]
avdernier_chiffre = numbers[-2]
if dernier_chiffre !=9:
    numbers[-1] = dernier_chiffre + 1
    print(numbers)
else:
    numbers[-2] = avdernier_chiffre + 1
    numbers[-1] = 0
    print(numbers)

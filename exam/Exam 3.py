romain_list = [
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000)
]

chromain=[]
input_len = int(input("sasir le nombre de chiffre voulu TABLEAU "))

for i in range(input_len):
    val=str(input(f"entre vos chiffre romain { i + 1 } ;"))
    chromain.append(val)

chromain.sort()
total=0
for symbole in chromain:
    for symbole_list, valeur in romain_list:
        if symbole == symbole_list:
            total += valeur
            break
print("Valeur totale =", total)        
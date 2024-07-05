
print("---------------------------------")
print("Andares de 20 a 1 com exclusão do 13 utilizando for loop")
for i in range(20,0,-1):
    if(i == 13):
        continue
    print(i)

print("---------------------------------")
print("Andares de 20 a 1 com exclusão do 13 utilizando while")
contador = 20
while contador != 0:
    if(contador == 13):
        contador -= 1
        continue
    print(contador)
    contador -= 1
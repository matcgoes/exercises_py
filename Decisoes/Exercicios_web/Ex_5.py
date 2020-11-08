# Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.

n=int(input("Quantos termos terá a série? "))
termo_a=1
termo_b=1
total=0
for i in range(1,n+1):
    print(str(termo_a)+"/"+str(termo_b))
    if n==1:
        total = (termo_a/termo_b)
    else:
        total = (termo_a/termo_b) + total
    termo_a=termo_a+1
    termo_b=termo_b+2
print("Soma total: ", total)


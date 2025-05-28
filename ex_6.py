'''
6. Solicite 5 números ao usuário e armazene em uma lista.
Em seguida, imprima o maior e o menor número.
'''

nums = [int(input("Digite um número: ")) for _ in range(5)]

print("Maior:", max(nums))
print("Menor:", min(nums))
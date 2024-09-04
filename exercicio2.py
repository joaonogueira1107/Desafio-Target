def verificaLetraA(palavra):
    contagem_a = palavra.lower().count('a')
    
    existe_a = contagem_a > 0
    
    return existe_a, contagem_a


palavra = input("Digite uma string para verificar a letra 'a': ")
    
existe_a, contagem_a = verificaLetraA(palavra)
    
if existe_a:
    print(f"A letra 'a' (maiúscula ou minúscula) ocorre {contagem_a} vez(es) na string.")
else:
    print("A letra 'a' (maiúscula ou minúscula) não ocorre na string.")


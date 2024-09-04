def confereNumero(n):
    if n < 0:
        return False
    
    a, b = 0, 1

    while b < n:
        a, b = b, a + b

    return b == n


try:
    numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))
        
    if confereNumero(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
    
except ValueError:
    print("Por favor, insira um número inteiro válido.")


# Questão 2: Sequência de Fibonacci e verificação de pertencimento

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def pertence_fibonacci(num):
    seq = fibonacci(num)
    return num in seq

# Você pode alterar este valor ou solicitar input do usuário
numero = 21

seq = fibonacci(numero)
pertence = pertence_fibonacci(numero)

print(f"Sequência de Fibonacci até {numero}: {seq}")
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
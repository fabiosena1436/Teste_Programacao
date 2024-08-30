# Questão 5: Inversão de string

def inverter_string(s):
    return ''.join(s[i] for i in range(len(s)-1, -1, -1))

# Exemplo de uso
texto = "Hello, World!"
texto_invertido = inverter_string(texto)

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
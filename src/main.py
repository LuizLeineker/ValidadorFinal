from regular import reconhecer_cpf
from livre_contexto import reconhecer_parenteses
from recursiva import reconhecer_w_w

## parte 6 - testando na pratica o dfa, pda, mt
## depois remover aqui 
print("=== TESTE DFA ===")
print(reconhecer_cpf("123.456.789-10"))
print(reconhecer_cpf("127.453.789-10"))
print(reconhecer_cpf("12345678910"))

print()

print("=== TESTE PDA ===")
print(reconhecer_parenteses("(()())"))
print(reconhecer_parenteses("(()"))

print()

print("=== TESTE MT ===")
print(reconhecer_w_w("101#101"))
print(reconhecer_w_w("101#100"))
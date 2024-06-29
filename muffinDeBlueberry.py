saldo_inicial = 500

def sacar(valor):
    if saldo_inicial >= valor:
        
        print("Valor sacado.\nRetire o seu dinheiro na boca do caixa.")
  
        saldo_final = saldo_inicial - saque

        print(f"Seu novo saldo é {saldo_final}")
        print("Obrigado por ser nosso cliente! :D")   
    else: print("Saldo insuficiente")

print("Seu saldo atual é de", saldo_inicial)

saque = float(input("Qual valor a ser sacado? "))
sacar(saque)

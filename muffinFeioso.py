saldo_inicial = 500

print("Seu saldo atual é de", saldo_inicial)
print("[1]SAQUE \n[2]DEPÓSITO \n[3]EXTRATO")
opcao = int(input("Digite uma opção: "))


if opcao == 1:
    
    valor_saque = float(input("Digite o valor a ser sacado: "))
    saldo_final = saldo_inicial - valor_saque

    if valor_saque >= saldo_inicial:
        print(f"Retire seu dinheiro.\nSeu saldo atual é de {saldo_final}")
    
    else: valor_saque <= saldo_inicial
    print("Saldo insuficiente")

elif opcao == 2:
    
    valor_deposito = float(input("Digite o valor a ser depositado: "))
    saldo_final = saldo_inicial + valor_deposito
    
    print(f"Obrigada pelo depósito. Seu saldo é de {saldo_final}")

elif opcao == 3:
    
    print(f"Saldo atual é de {saldo_inicial}")

else:
    
    print("Opção inválida...")
print("Bem vindo ao quiz")
usuario = input("Vamos começar?")
score = 0

if usuario == "S":
    print("Começando...")
    print("Quem é o criador do Minecraft? \n (A) Steven \n (B)Notch")

    resposta1 = input("Resposta: ")
    if resposta1 == "B":
        print("Resposta correta")
        score = score + 1
    else:
        print("Resposta errada")

    print("Qual é o nome verdadeiro do Notch?? \n (A) Markus Person \n (B) Marcos Machado")
    resposta1 = input("Resposta: ")
    if resposta1 == "A":
        print("Resposta correta")
        score = score + 1
    else:
        print("Resposta errada")

    print("Qual é o ano em que foi lançado? \n (A) 2011 \n (B) 2009")
    resposta1 = input("Resposta: ")
    if resposta1 == "B":
        print("Resposta correta")
        score = score + 1
    else:
        print("Resposta errada")

print(f"Finalizando... Sua pontuação foi de {score} acertos")

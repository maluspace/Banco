import random

animais = ["cachorro", "gato", "elefante", "leão", "tigre", "girafa", "zebra", "macaco", "coelho", "urso", "cavalo", "ovelha", "porco", "vaca", "galinha", "pato", "peixe", "tartaruga", "crocodilo", "jacaré", "cobra", "aranha", "abelha", "formiga", "borboleta", "vespa", "pavão", "coruja", "falcão", "águia"]

palavra_sorteada = random.choice(animais)
letras_acertadas = ''
tentativas = 0

while True:
    print("=== Jogo de Palavras ===")
    print("Tente adivinhar a palavra sorteada! \nDica: É um animal.")
    
    tentativa = input("Digite uma letra: ").strip().lower()

    if len(tentativa) != 1:
        print("Por favor, digite apenas uma letra.")
        continue
    else:
        tentativas += 1
        print(f"Você tentou {tentativas} vezes.")

        if tentativa in letras_acertadas:
            print("Você já tentou essa letra antes!") 
        
        elif tentativa in palavra_sorteada:
            letras_acertadas += tentativa
            print(f"Letra correta! \nLetras acertadas até agora: {letras_acertadas}")

        else:
            print("Letra incorreta!")


    for letra_secreta in palavra_sorteada:
        if letra_secreta in letras_acertadas:
            print(letra_secreta)
        else:
            print("*")

    acertou = True
    
    for letra_secreta in palavra_sorteada:
            if letra_secreta not in letras_acertadas:
                acertou = False
                break       

    if acertou:
            print("Parabéns, você acertou a palavra!")
            break
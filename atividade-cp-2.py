# ERICK KUWAHARA DA SILVA
# RM: 550371
# TURMA: 1TDSPN

# ================ SUBALGORITMOS

def verifica_email(email: str)  -> None:
    partes = email.split("@")

    if len(partes) != 2:
        errado()
        return

    parte_1_nome = partes[0]
    parte_2_dominio = partes[1]

    if parte_1_nome[0].isnumeric():
        errado()
        return

    caracteres_especiais = "!@#$%^&*()_+{}[]:;<>,?~\\|-/"
    for caracter in parte_1_nome:
        if caracter in caracteres_especiais:
            errado()
            return
    for caracter in parte_2_dominio:
        if caracter in caracteres_especiais:
            errado()
            return
    
    if parte_2_dominio.count(".") < 1 or parte_2_dominio.count(".") > 2:
        errado()
        return
    if ".." in parte_2_dominio:
        errado()
        return
    if parte_2_dominio.index(".") == 0:
        errado()
        return
    if parte_2_dominio.count(".") < 1:
        errado()
        return
    if parte_2_dominio[-1] == ".":
        errado()
        return

    correto(email)
    return True

def correto(email: str) -> None:
    arq = open("RM550371.txt", "w", encoding="utf-8")
    arq.write(email)
    arq.close()

def errado() -> None:
    print("E-mail inválido, digite outro correto!")

# ================ PROGRAMA PRINCIPAL

while True:
    email = input("Digite o e-mail: ")
    registro = verifica_email(email)

    if registro == True:
        print("\n Gravado com sucesso!")
        break

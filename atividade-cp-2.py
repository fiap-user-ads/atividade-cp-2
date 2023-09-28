# ERICK KUWAHARA DA SILVA
# RM: 550371
# TURMA: 1TDSPN

import os

# ================ SUBALGORITMOS 

def verifica_email(email: str)  -> None:
    errado()
    print("Func")

def correto() -> None:
    print("Correto")

def errado() -> None:
    print("E-mail inválido, digite outro correto!")

# ================ PROGRAMA PRINCIPAL

while True:
    os.system("cls")
    
    email = input("Digite o e-mail: ")
    verifica_email(email) 

    
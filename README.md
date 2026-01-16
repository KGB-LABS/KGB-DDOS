# KGB PUNCH DDOS


## ⚠️ AVISO LEGAL E USO ÉTICO ⚠️

Este projeto, **KGB PUNCH DDOS**, é uma ferramenta de simulação de ataque de negação de serviço (DDoS) desenvolvida **EXCLUSIVAMENTE PARA FINS EDUCACIONAIS** e para estudo de segurança de redes.

> **O uso desta ferramenta contra qualquer sistema, rede ou serviço sem a permissão expressa e prévia do proprietário é estritamente proibido e constitui crime sob a legislação brasileira e internacional.**

O desenvolvedor e os contribuidores deste projeto não se responsabilizam por qualquer uso indevido ou ilegal desta ferramenta. Utilize-a apenas em ambientes controlados, como redes de teste (sandboxes) ou sistemas próprios, onde você tenha total autoridade para realizar testes de estresse.

## 📚 Sobre o Projeto

O **KGB PUNCH DDOS** é um script simples em Python que simula um ataque de inundação UDP (UDP Flood). Ele foi projetado para demonstrar como um ataque DDoS de camada 4 (transporte) pode ser executado, enviando um grande volume de pacotes UDP para um alvo, com o objetivo de sobrecarregar a rede ou o serviço.

O script utiliza a biblioteca `pyfiglet` para um banner estilizado e a biblioteca `socket` para a comunicação de rede.

## ✨ Funcionalidades

*   Simulação de ataque de inundação UDP.
*   Rotação de portas de destino (de 1 a 65534) para maior dispersão do tráfego.
*   Interface de linha de comando simples para inserção de IP e porta de destino.
*   Contador de pacotes enviados.

## ⚙️ Instalação

Para utilizar o **KGB PUNCH DDOS**, você precisará ter o **Python 3** e o **git** instalados em seu sistema.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/allen-hub-dev/KGB-DDOS.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd KGB-DDOS
    ```

3.  **Instale as dependências:**
    O script requer a biblioteca `pyfiglet`.
    ```bash
    pip install -r requirements.txt
    ```

    > **Nota:** Certifique-se de que o arquivo `requirements.txt` no seu repositório contenha a linha `pyfiglet`.

## ▶️ Como Usar

Execute o script a partir do diretório do projeto:

```bash
python KGB-DDOS.py
```

O script solicitará as seguintes informações:

1.  **IP Alvo:** O endereço IP do sistema que você deseja testar (Lembre-se: **SOMENTE** sistemas próprios ou autorizados).
2.  **Porta de Início:** A porta inicial para o ataque. O script irá incrementar a porta a cada pacote enviado.

Para interromper o ataque, pressione `Ctrl + C`.

## 🤝 Contribuição

Contribuições são bem-vindas! Se você deseja melhorar o código, adicionar funcionalidades ou corrigir bugs, sinta-se à vontade para abrir uma *Issue* ou enviar um *Pull Request*.



---
*Desenvolvido para fins educacionais e de estudo de segurança de redes.*

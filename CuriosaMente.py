import os
import random
import requests # pip install requests
import json 
import wikipedia # pip install wikipedia
import time
import re

# Configurar idioma da Wikipedia
wikipedia.set_lang('pt')

# Carregar os dados do JSON hospedado no GitHub
url = 'https://raw.githubusercontent.com/MosconiDih/CuriosaMente/refs/heads/main/assuntos.json' # link público para consumo de assuntos para consulta
response = requests.get(url)
if response.status_code == 200:
    assuntos = response.json()  # Conteúdo do JSON com as categorias e tópicos
else:
    print("Falha ao carregar os dados. Código de status:", response.status_code)
    assuntos = {}  # Opcional: pode definir dados padrão ou encerrar o programa

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    limpar_terminal()
    print("Escolha uma categoria:")
    for i, categoria in enumerate(assuntos.keys(), start=1):
        print(f"{i}. {categoria.capitalize()}")

    try:
        escolha = int(input("\nDigite o número correspondente: "))
        if 1 <= escolha <= len(assuntos):
            categoria_selecionada = list(assuntos.keys())[escolha - 1]
            topicos = assuntos[categoria_selecionada]
            artigo = random.choice(topicos)

            # Buscar resumo do artigo na Wikipedia
            try:
                resumo = wikipedia.summary(artigo, sentences=5)
                pagina = wikipedia.page(artigo)

                # Divide o texto sempre que encontrar '.' ou '!', mantendo a pontuação e removendo espaços extras
                frases = re.split(r'(?<=[.!])\s+', resumo)
                resumo_formatado = "\n".join(frases)

                print(f"\nCuriosidade sobre {artigo}:")
                print(resumo_formatado)
                print("\nPara aprender mais sobre esse assunto, acesse:", pagina.url)
            except Exception as e:
                print(f"Não foi possível recuperar informações para {artigo}: {e}")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")

    voltar = input("\nDeseja voltar às opções? (s/n): ").strip().lower()
    if voltar != 's':
        limpar_terminal()
        print("Encerrando o programa. Espero que você tenha aprendido algo novo hoje!")
        time.sleep(1)
        print("Volte aqui para a sua pílula de conhecimento sempre que quiser!")
        time.sleep(3)
        limpar_terminal()
        break

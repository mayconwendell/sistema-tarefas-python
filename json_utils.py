import json

def salvar_tarefas(tarefas):

    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def carregar_tarefas():
    try:
            
        with open("tarefas.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
        
    except FileNotFoundError:
        tarefas = []
        return tarefas
 
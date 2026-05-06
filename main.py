import json

def menu(tarefas):

    while True:
        print('1 - Adicionar tarefa' \
        '\n2 - Ver tarefas' \
        '\n3 - Remover tarefas' \
        '\n4 - Marcar como concluída' \
        '\n5 - Sair')
        try: 
            opcao = int(input('Digite a opção que deseja: '))

            if opcao == 1:
                adicionar_tarefas(tarefas)
            
            elif opcao == 2:
                ver_tarefas(tarefas)
            
            elif opcao == 3:
                remover_tarefas(tarefas)

            elif opcao == 4:
                marcar_como_concluida(tarefas)
            elif opcao == 5:
                print('Programa encerrado!')
                salvar_tarefas(tarefas)
                break
            
            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')

def adicionar_tarefas(tarefas):
    continuar = 's'

    while continuar == 's':

        nome = input('Digite a tarefa que deseja adicionar: ')

        novas_tarefas = {
            'nome': nome,
            'concluida': False
        }

        tarefas.append(novas_tarefas)
        print('Tarefa adicionada com sucesso!')

        continuar = input('Deseja adicionar uma nova tarefa? (s / n) ').lower().strip()

def ver_tarefas(tarefas):
    if not tarefas:
        print('Não tem tarefas cadastradas!')
        return

    else:
        print('==========Lista de Tarefas=========')
        for i, tarefa in enumerate(tarefas):

            status = "Concluida" if tarefa['concluida'] else "Pendente"

            print(f"{i + 1} - {tarefa['nome']} - {status}")        
        

def marcar_como_concluida(tarefas):
    
    if not tarefas:
        print('Não tem tarefas cadastradas!')
        return
    else:
        continuar = 's'

        while continuar == 's':

            try:
                ver_tarefas(tarefas)         
                pergunta = int(input('Qual tarefa deseja marcar como concluída: '))

                if pergunta > 0 and pergunta <= len(tarefas):    
                    indice = pergunta - 1

                    if tarefas[indice]['concluida'] == False:

                        tarefas[indice]['concluida'] = True
                        print('A tarefa foi marcada como concluída!')

                    else:
                        print('A tarefa escolhida já foi concluída!')    
                else:
                    print('Você digitou uma opção inválida!')

            except ValueError:
                print('Valor digitado inválido!')

            continuar = input('Deseja marcar outra tarefa como concluída? (s / n) ').lower().strip()

def remover_tarefas(tarefas):
    
    if not tarefas:
        print('Não tem tarefas cadastradas!')
        return
    else:
        continuar = 's'
        
        while continuar == 's':
            try:

                ver_tarefas(tarefas)
                pergunta = int(input('Qual tarefa deseja remover: '))

                if pergunta > 0 and pergunta <= len(tarefas):
                    
                    indice = pergunta - 1
                    tarefas.pop(indice)
                    print('Tarefa removida com sucesso!')

                else:
                    print('Você digitou um opção inválida!')

            except ValueError:
                print('Valor digitado inválido!')

            continuar = input('Deseja remover outra tarefa? (s / n) ').lower().strip()

def salvar_tarefas(tarefas):

    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)


def carregar_tarefas():
    try:
            
        with open("tarefas.json", "r") as arquivo:
            dados = json.load(arquivo)
            return dados
        
    except FileNotFoundError:
        tarefas = []
        return tarefas
    
tarefas = carregar_tarefas()
menu(tarefas)
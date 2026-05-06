tarefas = []

def menu():

    while True:
        print('1 - Adicionar tarefa' \
        '\n2 - Ver tarefas' \
        '\n3 - Sair')
        try: 
            opcao = int(input('Digite a opção que deseja: '))

            if opcao == 1:
                adicionar_tarefas()
            
            elif opcao == 2:
                ver_tarefas()
            
            elif opcao == 3:
                print('Programa encerrado!')
                break
            
            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')

def adicionar_tarefas():
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

def ver_tarefas():
    if not tarefas:
        print('Não tem tarefas cadastradas!')
        return

    else:
        print('==========Lista de Tarefas=========')
        for i, tarefa in enumerate(tarefas):

            status = "Concluida" if tarefa['concluida'] else "Pendente"
            
            print(f"{i + 1} - {tarefa['nome']} - {status}")        
        
menu()
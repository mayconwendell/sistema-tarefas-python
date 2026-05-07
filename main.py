import json

def menu(tarefas):

    while True:
        print('\n========== MENU =========')
        print('\n1 - Adicionar tarefa' \
        '\n2 - Ver tarefas' \
        '\n3 - Remover tarefas' \
        '\n4 - Marcar como concluída' \
        '\n5 - Editar tarefas' \
        '\n6 - Sair\n')
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
                editar_tarefas(tarefas)

            elif opcao == 6:
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
        existe = False

        for tarefa in tarefas:

            if nome == tarefa['nome']:
                existe = True
                
        if existe == True:
            print('A tarefa digitada já está adicionada!')

        else:

            print('1 - Alta' \
            '\n2 - Média' \
            '\n3 - Baixa\n')

            try:
                prioridade = int(input('Prioridade da tarefa: '))
                prioridade_valida = True

                if prioridade == 1:
                    prioridade = "Alta"

                elif prioridade == 2:
                    prioridade = "Média"

                elif prioridade == 3:
                    prioridade = "Baixa"
                
                else:
                    print('Você digitou um número inválido')
                    prioridade_valida = False

                if prioridade_valida == True:

                    novas_tarefas = {
                        'nome': nome,
                        'concluida': False,
                        'prioridade': prioridade
                    }

                    tarefas.append(novas_tarefas)
                    print('Tarefa adicionada com sucesso!')

            except ValueError:
                print('Valor digitado inválido!')

        continuar = input('Deseja adicionar uma nova tarefa? (s / n) ').lower().strip()

def ver_tarefas(tarefas):
    if not tarefas:
        print('Não tem tarefas cadastradas!')
        return

    else:
        print("\n1 - Ver todas"
        "\n2 - Ver concluídas"
        "\n3 - Ver pendentes"
        "\n4 - Ver prioridade alta" \
        "\n5 - Ver prioridade média" \
        "\n6 - Ver prioridade baixa"
        "\n7 - Voltar\n")
        try:
                
            opcao = int(input('Digite a opção que deseja: '))

            if opcao < 1 or opcao > 7:
                    print("Opção inválida!")
                    return
            
            elif opcao == 7:
                return
                
            else:

                for i, tarefa in enumerate(tarefas):

                    status = "✅ Concluida" if tarefa['concluida'] else "⏳ Pendente"
            
                    if opcao == 1:
                        print(f"{i + 1} - {tarefa['nome']} - {status} - {tarefa['prioridade']}")        
                
                    elif opcao == 2:
                        if tarefa['concluida']:
                            print(f"{i + 1} - {tarefa['nome']} - {status}")

                    elif opcao == 3:
                        if not tarefa['concluida']:
                            print(f"{i + 1} - {tarefa['nome']} - {status} - {tarefa['prioridade']}")
                    
                    elif opcao == 4:
                        if tarefa['prioridade'] == "Alta":
                            print(f"{i + 1} - {tarefa['nome']} - {status} - {tarefa['prioridade']}")

                    elif opcao == 5:
                        if tarefa['prioridade'] == "Média":
                            print(f"{i + 1} - {tarefa['nome']} - {status} - {tarefa['prioridade']}")

                    elif opcao == 6: 
                        if tarefa['prioridade'] == "Baixa":
                            print(f"{i + 1} - {tarefa['nome']} - {status} - {tarefa['prioridade']}")

        except ValueError:
            print('Você digitou um valor inválido!')
             
def editar_tarefas(tarefas):
    
    if not tarefas:
        print('Não tem tarefas cadastradas!')
    else:
        continuar = 's'
        while continuar == 's':

            try:

                ver_tarefas(tarefas)

                pergunta = int(input('Qual tarefa deseja editar: '))

                if pergunta > 0 and pergunta <= len(tarefas):
                    indice = pergunta - 1
                    print('1 - Editar nome'
                    '\n2 - Editar prioridade'
                    '\n3 - Voltar\n')

                    opcao = int(input('Qual opção deseja: '))
                
                    if opcao == 1:
                        novo_nome = input('Digite o novo nome: ')
                        tarefas[indice]['nome'] = novo_nome
                        print('Nome alterado com sucesso!')
                    
                    elif opcao == 2:

                        print('1 - Alta' \
                            '\n2 - Média' \
                            '\n3 - Baixa\n')
                        
                        nova_prioridade = int(input('Qual a nova prioridade: '))
                        prioridade_valida = True

                        if nova_prioridade  == 1:
                            nova_prioridade  = "Alta"

                        elif nova_prioridade  == 2:
                            nova_prioridade  = "Média"

                        elif nova_prioridade == 3:
                            nova_prioridade = "Baixa"
                        
                        else:
                            print('Você digitou um número inválido')
                            prioridade_valida = False

                        if prioridade_valida == True:
                            tarefas[indice]['prioridade'] = nova_prioridade
                            print('Prioridade alterada com sucesso!')

                    elif opcao == 3:
                        break
                    
                    else:
                        print('Opção inválida!')
                else:
                    print('Você digitou uma tarefa inválida!')
                        
            except ValueError:
                print('Você digitou um valor inválido!')
            
            continuar = input('Deseja editar outra tarefa? (s / n) ').lower().strip()

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
        json.dump(tarefas, arquivo, indent=4)


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
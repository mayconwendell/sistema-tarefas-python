from tarefas import adicionar, remover, editar, ver, concluir
from json_utils import salvar_tarefas, carregar_tarefas

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
                adicionar(tarefas)
            
            elif opcao == 2:
                ver(tarefas)
            
            elif opcao == 3:
                remover(tarefas)

            elif opcao == 4:
                concluir(tarefas)

            elif opcao == 5:
                editar(tarefas)

            elif opcao == 6:
                print('Programa encerrado!')
                salvar_tarefas(tarefas)
                break
            
            else:
                print('Opção inválida!')

        except ValueError:
            print('Você digitou um valor inválido!')
   
tarefas = carregar_tarefas()
menu(tarefas)
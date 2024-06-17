'''
Tera uma lista de alunos, com as notas de b1 e b2, um menu para selecionar as opções.
1 - aicionar aluno
2 - listar alunos
3 - remover aluno
4 - procurar aluno
5 - aprovado
6 - reprovado
7 - procurar pelo nome do aluno
8 - Media da turma B1
9 - media da turma b2
10 - media da turma GERAL
0 - sair
'''

alunos = {}
text = print("Diario da turma")

def menu():
    print("1 - adicinar aluno")
    print("2 - listar alunos")
    print("3 - remover aluno")
    print("4 - procurar aluno")
    print("5 - aprovados")
    print("6 - reprovados")
    print("7 - Procurar pelo nome do aluno")
    print("8 - Media da turma B1")
    print("9 - media da turma b2")
    print("10 - media da turma GERAL")
    print("11 - Diario aluno")
    print("0 - sair")
    try:
        opt = int(input("Digite a opção: "))
        return opt
    # except KeyboardInterrupt:
    #    print("Deu pau no teclado")
    # except ValueError:
    #    print("Numero digitado errado!")
    except Exception as e:
        print(f"Digite um numero: {e}")
        return 9
    #   finally:
    #       print("Mostra isso!")

def add_aluno():
    try:
        ra = input("Digite o Ra do aluno: ")
        nome = input("Digite o nome do alino: ")
        nota_b1 = float(input("Dgiite  a nota B1 do aluno: "))
        nota_b2 = float(input("Digite a nota B2 do aluno: "))
        dados = {"nome": nome, "b1": nota_b1, "b2": nota_b2}
        alunos[ra] = dados
    except Exception as e:
        print(f"Alguma coisa foi digitada errado{e}")
    input("pressione qualquer tecla para continuar")
    
def remover_alunos():
    ra = input("Digite o RA do Aluno: ")
    if ra in alunos:
        aluno = alunos.pop(ra)
        print(f"O aluno:{aluno["nome"]} foi removido")
    else:
        print("Aluno não encontrado!")
    input("Pressione qualquer tecla para continuar")
    
def listar_alunos():
    for ra, dados in alunos.items():
        print(f"RA: {ra} - Nome: {dados["nome"]} - B1: {dados["b1"]} - B2: {dados["B2"]}")
        # print(ra, dados)
def procurar_aluno():
    ra = input('digite o RA do aluno: ')
    if ra in alunos:
        dados = alunos[ra]
        print(f'RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']}')
    else:
        print('aluno não encontrado')
        input('pressione qualquer tecla para continuar')
def aprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) / 2) < 7:
            aluno = f"RA: {ra} -"
            aluno += f"Nome: {dados["nome"]}"
            aluno += f"B1: {dados["b1"]}"
            aluno += f"B2: {dados["b2"]}"
            print(aluno)
    input('pressione qualquer tecla para continuar')

def reprovados():
    for ra, dados in alunos.items():
        if ((dados["b1"] + dados["b2"]) / 2) < 7:
            aluno = f"RA: {ra} -"
            aluno += f"Nome: {dados["nome"]}"
            aluno += f"B1: {dados["b1"]}"
            aluno += f"B2: {dados["b2"]}"
            print(aluno)
    input('pressione qualquer tecla para continuar')

def procurar_pelo_nome_do_aluno():
    nome = input('digite o Nome do aluno: ')
    if nome in alunos:
        dados = alunos[nome]
        print(f'RA: {ra} - Nome: {dados['nome']} - B1: {dados['b1']} - B2:{dados['b2']}')
        input("Pressione qualquer tecla para continuar")
    else:
        print('aluno não encontrado')
        input('pressione qualquer tecla pa')
def media_geral():
    soma = 0
    qtd = 0
    for dados in alunos.values():
        soma += dados["b2"]
        qtd += 1
    media = soma /qtd
    print(f"A media geral da turma é: {media:.2f}")
    input("pressione qualquer tecla para continuar")

def media_b1():
    total_notas = 0
    total_alunos = 0
    for dados in alunos.values():
        total_notas += dados['b1']
        total_alunos += 1
    media_b1 = total_notas / total_alunos
    print(f'Média da turma na B1: {media_b1:.2f}')
    input('Pressione qualquer tecla para continuar')
    
def media_b2():
    total_notas = 0
    total_alunos = 0
    for dados in alunos.values():
        total_notas += dados['b2']
        total_alunos += 1
    media_b2 = total_notas / total_alunos
    print(f'Média da turma na B2: {media_b2:.2f}')
    input('Pressione qualquer tecla para continuar')

def diario_aluno():
    c1 =("-") 
    print(c1.ljust(56, "-"))
    print("                  Diário da turma")
    print(c1.ljust(56, "-"))
    print("RA    Nome                      Nota B1  Nota B2  Média")
    print(c1.ljust(56, "-"))
    
    soma_b1 = soma_b2 = soma_geral = 0
    contador = 0
    
    for ra, dados in alunos.items():
        media = (dados['b1'] + dados['b2']) / 2
        soma_b1 += dados['b1']
        soma_b2 += dados['b2']
        soma_geral += media
        contador += 1
        print(f"{ra.ljust(5)} {dados['nome'].ljust(27)} {str(dados['b1']).rjust(5)}  {str(dados['b2']).rjust(5)}   {str(media).rjust(5)}")
    
    if contador > 0:
        media_b1 = soma_b1 / contador
        media_b2 = soma_b2 / contador
        media_geral = soma_geral / contador
    else:
        media_b1 = media_b2 = media_geral = 0
    
    print(c1.ljust(56, "-"))
    print(f"{'Médias da Turma'.ljust(32)}  {str(media_b1).rjust(5)}  {str(media_b2).rjust(5)}   {str(media_geral).rjust(5)}")
    print(c1.ljust(56, "-"))
    input("clique em qualquer lugar, para continuar ") 


    
if __name__ == '__main__':
    while True:
        match menu():
            case 1:
                add_aluno()
            case 2:
                listar_alunos()
            case 3:
                remover_alunos()
            case 4:
                procurar_aluno()
            case 5:
                aprovados()
            case 6:
                reprovados()
            case 7:
                procurar_pelo_nome_do_aluno()
            case 8:
                media_b1()
            case 9:
                media_b2()
            case 10:
                media_geral()
            case 11: 
                diario_aluno()
                break

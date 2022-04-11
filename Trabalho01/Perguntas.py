#Matheus Roberto Barcellos Ferraz

from Trabalho.Grupo import Grupo
from Trabalho.Funcionario import Funcionario
from Trabalho.Escolaridade import Escolaridade
from Trabalho.Empresa import Empresa
from Trabalho.Departamento import Departamento
from Trabalho.Pais import Pais
from Trabalho.Filial import Filial
from Trabalho.Cidade import Cidade
from Trabalho.Estado import Estado

questao = int(input('Digite o número da questão(apenas números de 1~5:)'))
grupo = Grupo('Zona Norte', 'Jorge dos Santos', 'São Paulo')
escolaridade = Escolaridade('PhD')
pais = Pais('Brasil')
funcionario = Funcionario('Ana Portela', '297841-8', 'Auxiliar Administrativo', 'Portugal', 'Carlos Henrique Casimiro')
filial = Filial('Loja 02')
cidade = Cidade('Teresina')
estado = Estado('Piauí')
departamento = Departamento('Setor Jurídico', 'Mateus Sarlo')
empresa = Empresa('Dicão petshop', 'Maria Eduarda Carmo')

if questao == 1:
    escolaridade = Escolaridade('PhD')
    print('1) Qual a escolaridade do presidente de um grupo?')
    print()
    print(f'O presidente {grupo.getPresidente()}do grupo {grupo.getNome()} possui um {escolaridade.getEscolaridade()}.')

else:
    escolaridade = Escolaridade('Mestrado')
    if questao == 2:
        print('2) Qual o país de alocação de um funcionário?')
        print()
        print(f'O funcionário {funcionario.getNome()} foi alocado para a sede de Porto no país {funcionario.getAlocacao()}.')

    else:
        if questao == 3:
            print('3) Qual o estado da filial que um funcionário coordena?')
            print()
            print(f'A filial {filial.getNomefilial()}, no estado de {estado.getNomeestado()}, é comandada pelo funcionário {funcionario.getCoordenacao()}. ')

        else:
            if questao == 4:
                print('4) Qual a escolaridade do chefe de um departamento?')
                print()
                print(f'O chefe {departamento.getChefia()} do {departamento.getNomedepartamento()} possui escolaridade máxima de {escolaridade.getEscolaridade()}.')

            else:
                if questao == 5:
                    print('5) Qual o nome do diretor da empresa de uma filial?')
                    print(f'A pessoa que ocupa o cargo de diretoa da {empresa.getNomeempresa()} é a {empresa.getDiretor()}, responsável pela filial {filial.getNomefilial()}.')
                else:
                    print('Número de questão inválida!')

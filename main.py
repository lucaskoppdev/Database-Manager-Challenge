#banco de dados relacional com python from scratch

from commands import *

#Listas "CORE" do programa
database = []
database_column_names = []


#Cria colunas no banco de dados, e da um nome numa lista que vai ser usada para armaazenar o nome das colunas
def database_newcolumn():
    column_name = input("Digite o nome da nova coluna ->")
    database_column_names.append(column_name)
    database.append([])


def display_columns():
    print("----------> colunas do banco <----------\n")
    for column in database_column_names:
        print(column, end = "|| ")
    print("")
    print("----------------------------------------\n")
    


def acess_column_byname():
    user_input = input("Digite o nome da coluna que deseja acessar ->")
    
    try:
        for index, value in enumerate(database_column_names): #retorna indice e nome da coluna
            if user_input == value:
                return index
    
    except KeyError:
        return "colunao nao existente!"



def insert_line_value():

    database_index = acess_column_byname()

    number_lines = int(input("Digite a quantidade de linhas para criar na coluna->"))

    column_create_lines = database[database_index]

    for i in range(number_lines):
        valor_input = input(f"Digite o valor a adicionar na coluna {i}->")

        column_create_lines.append(valor_input)



def remove_database_column_byname():

    column = acess_column_byname()#Inicialmente nao e necessario tratar erros aqui, pois essa tarefa ja esta delegada na fu
    
    del database_column_names[column]
    del database[column]



def display_columns_with_line_values():
    print("----------> colunas do banco <----------\n")
    for column in database_column_names:
        print(column, end = "|| ")

    print("\n")

    for linha in database:
        for valor in linha:
            print(valor, end = "||")
        print("\n")



def remove_column_line_byvalue():
    
    database_index = acess_column_byname()

    column = database[database_index]
   
    print("OBS: PRA CANCELAR A OPERACAO, DIGITE ->999<-")
    user_input = input("Digite o valor da linha->")
    
    if user_input == 999:
        print("Operacao cancelada com exito !")
        return None

    try:
        for index, value in enumerate(column):
            if value == user_input:
                del column[database_index]
                print("Coluna removida com sucesso!")
                return None
    except KeyError:
        return "Linha nao existente!"


def remove_column_line_byindex():
    database_index = acess_column_byname()
    
    column = database[database_index]

    print("-------VALORES DA COLUNA-------\n")
    for valor in column:
        print(valor, end = "||")
    
    print("OBS: PRA CANCELAR A OPERACAO, DIGITE ->999<-")
    line_pop = int(input("Digite o indice da linha que deseja remover->"))

    while True:
        if line_pop == 999:
            print("Operacao cancelada com Exito !")
            return None

        if line_pop > len(column):
            print("Indice inexistente, tente novamente ou aborte operacao !")
            continue
        

        del column[line_pop]

        return None

#comandos possiveis
print("exit, newcol, displaycol, insertline, displayvalues, removecolumn, removeline, removelinebyvalue")
    
    
#Main loop
while True:
    print("exit, newcol, displaycol, insertline, displayvalues, removecolumn, removeline, removelinebyvalue")
    action = command_line() 

    if action == 0:
        print("-----> ENCERRADO <------")
        brake
    
    if action == 1:
        database_newcolumn()
    
    if action == 2:
        display_columns()

    if action == 4:
        insert_line_value()

    if action == 5:
        display_columns_with_line_values()

    if action == 6:
        remove_database_column_byname()
        
    if action == 7:
        remove_column_line_byindex()
    
    if action == 8:
        remove_column_line_byvalue()
    
    else:
        print("Comando nao encontrado!")

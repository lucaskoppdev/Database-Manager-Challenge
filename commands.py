#Simulador de Comandos SQL em python puro from scratch
def command_line():

    #print(comandos)
    entrada = input(">")

    if entrada == "exit":
        return 0

    if entrada == "newcol":
        return 1

    if entrada == "displaycol":
        return 2

    if entrada == "insertline":
        return 4

    if entrada == "displayvalues":
        return 5

    if entrada == "removecolumn":
        return 6

    if entrada == "removeline":
        return 7
    
    if entrada == "removelinebyvalue":
        return 8


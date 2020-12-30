import sys

#Função para encontrar numero da linha que contém o argumemnto desejado
def get_line(txt):
    file = open('topol.top', encoding='utf8')
    for line_num, value in enumerate(file, 1): #le todas as linhas e valores do file começando como 1
        if txt in value:                       #qdo encontra o 'txt' retorna o valor da linha
            return line_num

if len(sys.argv) < 3:
    print('ERROR: put lig and cof names without extension')

else:
    # #Arguments
    lig = sys.argv[1]
    cof = sys.argv[2]

    #txt to find the line number and add after or before the arguments .prm and .itp
    x = str('#include "./charmm36-mar2019.ff/forcefield.itp"')
    y = str('; Include Position restraint file')
    z = str('Protein             1')

    #Open topol.top -> Read lines and add the argument .prm
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(x),f'\n; Include ligand parameters\n#include "{lig}.prm"\n#include "{cof}.prm"\n')
    file.seek(0)
    file.writelines(line)
    
    #Open topol.top -> Read lines and add the argument .itp
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(y)+ 4,f'; Include ligand topology\n#include "{lig}.itp"\n#include "{cof}.itp"\n\n')
    file.seek(0)
    file.writelines(line)
    
    #Open topol.top -> Read lines and add the argument final molecules number
    file = open('topol.top', 'r+', encoding='utf8')
    line = file.readlines()
    line.insert(get_line(z),f'\n{lig}                 1\n{cof}                 1')
    file.seek(0)
    file.writelines(line)

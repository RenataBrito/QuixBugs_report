#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import re

#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def rodar_mutmut(programa):

    test_comand = 'mutmut run --paths-to-mutate=/home/renata/Desktop/IC/novasAtividades/{}'.format(programa)  
        
    process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
    (stdout,stderr) = process.communicate()
    minha_string = stdout.decode("utf-8")    
    
    return minha_string

def processa_saida(saida, nome_programa):

    token = saida.find('2. Checking mutants')
 
    saida = saida[token:]

    lista  = saida.split()

    total  = lista[-9]
    mortos = lista[-7]
    timeout = lista[-5]
    suspeitos = lista[-3]
    vivos     = lista[-1] 

    vet_resp = [total, mortos, timeout, suspeitos, vivos]

    print('Name                                            ME/TM    MM     TL    Susp   SobV')
    print('---------------------------------------------------------------------------------')
    print('{}                                    '.format(nome_programa), end="  ")
    
    j = 0
    tam_vet_resp = len(vet_resp)

    while(j < tam_vet_resp ):
        print(vet_resp[j] + '      ', end="")
        j = j + 1
        if(j == tam_vet_resp):
            print('\n')



if __name__ == "__main__":

    for dir_name, subdir_list, file_list in os.walk(ROOT_DIR):

        if dir_name == ROOT_DIR +'/python_programs':
                
            for file_name in file_list:

                if file_name[-2:] == 'py':
                    print(file_name)
                    resultado = rodar_mutmut(file_name)
                    processa_saida(resultado, file_name)
    
    
    
    

    
    
     


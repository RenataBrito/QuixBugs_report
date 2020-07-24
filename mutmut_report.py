#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_mutmut(path, program):

    #comand line to run  mutmut
    test_comand = 'mutmut run --paths-to-mutate={}/{}'.format(path, program) 
    
    #runing mutmut using subprocess
    process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
    (stdout,stderr) = process.communicate()

    #get the output execution as a string
    output_string = stdout.decode("utf-8")    
    
    return output_string


def process_output(output_string, program):

    #find the part of the string that contains the results
    token = '2. Checking mutants'
    (before, token, after) = output_string.partition(token)

    #check if there are some valid mutants
    if after.strip() == '':

        results_list = ["-/-", "-", "-", "-", "-", "-"]
        result = {program: results_list}
        
        print("W: O programa {} não possui mutantes".format(program))
    
        return result

    else:
        #split the results into a list
        results_list  = after.split()

        #get the target data
        total      = results_list[-11]
        killed     = results_list[-9]
        timeout    = results_list[-7]
        suspicious = results_list[-5]
        survived   = results_list[-3]
        alive      = results_list[-1] 


        #update results_list with target data
        results_list = [total, killed, timeout, suspicious, survived, alive]

        result = {program: results_list}

        return result 


def print_results(result_dict):

    #printing the results
    cabecalho = ""
    title_ini = 'Name ME/TM KM  TL Susp SobV Skip'
    cabecalho_list = title_ini.split()
    for i in cabecalho_list:
        if(i == 'Name'):
            cabecalho = cabecalho + i + "                               "
            tam_esp_name = len(cabecalho)
        elif(i == 'Skip'):
            cabecalho = cabecalho + i
        else:
            cabecalho = cabecalho + i + "    "
    print(cabecalho)
    tam_cabecalho = len(cabecalho)
    while(tam_cabecalho != 0):
        if(tam_cabecalho == 1):
            print('-\n')
            tam_cabecalho = 0
        else:
            print('-', end="")
            tam_cabecalho = tam_cabecalho - 1
        
     
    for (key, values) in result_dict.items():
        i = 0
        name_program = ""
        espaco = ""
        #key is the name of the program
        #values are the results of the mutation testing
        tam_name = len('{}'.format(key))
        qtd_esp = tam_esp_name - tam_name
        while(qtd_esp > 0):
            espaco = espaco + " "
            qtd_esp = qtd_esp - 1

        name_program = '{}'.format(key) + espaco
        print(name_program, end=" ")
        for v in values:
            if((i== 0) and (len(v)==5)):
                print(v +'   ', end="")
            elif ((i==0)and(len(v)==3)):
                print(v +'     ', end="")
            elif ((i==1)and(len(v)==2)):
                print(v +'    ', end="")
            elif ((i==1)and(len(v)==1)):
                print(v +'     ', end="")
            elif ((i==2)and(len(v)==1)):
                print(v +'      ', end="")
            elif ((i==2)and(len(v)==2)):
                print(v +'     ', end="")
            elif ((i==3)and(len(v)==1)):
                print(v +'       ', end="")
            elif ((i==3)and(len(v)==2)):
                print(v +'      ', end="") 
            elif ((i==4)and(len(v)==1)):
                print(v +'       ', end="")
            elif ((i==4)and(len(v)==2)):
                print(v +'      ', end="")
            else:
                print(v,end="")

            i+=1
        print('\n')


if __name__ == "__main__":

    #target dir
    python_programs_dir = ROOT_DIR +'/python_programs'

    #store the results
    result_dict = {}

    #run for a single program
    if len(sys.argv) == 2:
        
        #read the program name
        python_program = str(sys.argv[1])

        #execute mutmut and save the results in the dictionary
        string_result = run_mutmut(python_programs_dir, python_program)
        result_dict = process_output(string_result, python_program)


    #run for all programs
    else:

        #walk into the dirs of the project
        for dir_name, subdir_list, file_list in os.walk(ROOT_DIR):

            #will run only on python_programs_dir
            if dir_name == python_programs_dir:

                #check every file into the dir    
                for python_program in file_list:
                    
                    #run the task if it's a python file
                    if python_program[-2:] == 'py':
                        
                        #execute mutmut and get the results
                        string_result = run_mutmut(python_programs_dir, python_program)
                        results = process_output(string_result, python_program)

                        #add the results in the final dictionary
                        result_dict.update(results) 

    #after get all the results, print in the screen
    print_results(result_dict)
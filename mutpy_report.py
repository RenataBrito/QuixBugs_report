#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import shutil
#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_mutpy(path, program):
    if program == 'node.py':
        return '[*] Mutation score [0]: 0% - all: - - killed: - (0%) - survived: - (0.0%) - incompetent: - (0.0%)   - timeout: - (0%) [*] Coverage: 0 of 0 AST nodes (-)'
    else:
        array_files_copy = []
        src = ROOT_DIR +'/python_tests'
        src2 = ROOT_DIR +'/python_programs'
        dst = ROOT_DIR
        #copy all tests
        files_tests = os.listdir(src)
        for file_test in files_tests:
            if(file_test=='test_'+program):
                array_files_copy.append(file_test)
                shutil.copy(src=src + '/' + file_test, dst=dst)
        #copy all programs
        file_programs = os.listdir(src2)
        for file_program in file_programs:
            if(file_program == program):
                array_files_copy.append(file_program)
                shutil.copy(src=src2 + '/' + file_program, dst=dst)
        #copy the node file, because it has more than 1 program that uses it
        file_node_program = os.listdir(src2)
        for file_node in file_node_program:
            if(file_node == 'node.py'):
                shutil.copy(src=src2 + '/' + file_node, dst=dst)
        #comand line to run  mutmut
        test_comand = 'mut.py --target {} --unit-test test_{} --runner pytest --coverage'.format(program,program)
        #runing mutmut using subprocess
        process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
        (stdout,stderr) = process.communicate()

        #get the output execution as a string
        output_string = stdout.decode("utf-8")
        #remove files whithout node file
        while(len(array_files_copy)!=0):
            file = array_files_copy[0]
            os.remove(file)
            array_files_copy.remove(file)
        #remove node file
        if(os.path.exists('node.py')):
            os.remove('node.py')
        
        return output_string


def process_output(output_string, program):

    #find the part of the string that contains the results
    token = 'Mutation score'
    (before, token, after) = output_string.partition(token)

    #split the results into a list
    results_list  = after.split()

    #get the target data
    ALL         = results_list[-25]
    Killed      = results_list[-22]
    Survived    = results_list[-18]
    Incompetent = results_list[-14]
    Timeout     = results_list[-10]
    Coverage    = results_list[-1] 

    #update results_list with target data
    results_list = [ALL, Killed, Survived, Incompetent, Timeout, Coverage]

    result = {program: results_list}

    return result 



def print_results(result_dict):

    #printing the results
    cabecalho = ""
    title_ini = 'Name ALL   Killed   Survived   Incompetent   Timeout   Coverage'
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
            if((i== 0) and (len(v)==1)):
                print(v +'       ', end="")
            elif ((i==0)and(len(v)==2)):
                print(v +'      ', end="")
            elif ((i==1)and(len(v)==1)):
                print(v +'          ', end="")
            elif ((i==1)and(len(v)==2)):
                print(v +'         ', end="")
            elif ((i==2)and(len(v)==1)):
                print(v +'             ', end="")
            elif ((i==2)and(len(v)==2)):
                print(v +'            ', end="")
            elif ((i==3)and(len(v)==1)):
                print(v +'            ', end="")
            elif ((i==3)and(len(v)==2)):
                print(v +'           ', end="")
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
        string_result = run_mutpy(python_programs_dir, python_program)
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
                        string_result = run_mutpy(python_programs_dir, python_program)
                        results = process_output(string_result, python_program)

                        #add the results in the final dictionary
                        result_dict.update(results) 

    #after get all the results, print in the screen
    print_results(result_dict)
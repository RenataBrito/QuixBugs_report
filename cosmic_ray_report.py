#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

#used to find the root dir of the projetct
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def run_a_program(sections_cosmic_ray,database_cosmic_ray,program):
    if(program == "node"):
        return
    else:
        #starts the section
        test_comand = 'cosmic-ray init {}/{}.toml {}/{}.sqlite'.format(sections_cosmic_ray, program,database_cosmic_ray,program)
        #runing starts section about cosmic ray using subprocess
        process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
        (stdout,stderr) = process.communicate()

        #Run the section
        test_comand = 'cosmic-ray exec {}/{}.sqlite'.format(database_cosmic_ray,program)
        #runing run about cosmic ray using subprocess
        process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
        (stdout,stderr) = process.communicate()

        #print at terminal
        test_comand = 'cr-report {}/{}.sqlite'.format(database_cosmic_ray,program)
        #runing output about cosmic ray using subprocess
        process = subprocess.Popen(test_comand, stdout=subprocess.PIPE, shell=True)
        (stdout,stderr) = process.communicate()

        #get the output execution as a string
        output_string = stdout.decode("utf-8")    
        return output_string

def process_output(output_string,program):
    if(program=="node"):
        results_list = ["-", "-", "-"]

        result = {program: results_list}

        return result 
    else:
        #find the part of the string that contains the results
        token = 'total jobs: '
        (before, token, after) = output_string.partition(token)

        #split the results into a list
        results_list = after.split()

        try:
            #get the target data
            total      = results_list[-7]
            killed     = results_list[-5]
            survived   = results_list[-1] 

        except FileNotFoundError as f:
            print("Outro erro: ",f)
    
        except IndexError as g:
            print("Outro erro: ",g)

        except Exception as e: 
            print("W: Problema no programa: {}".format(program) + "erro: ",  e)
            return {program: []}

        results_list = [total, killed, survived]
        result = {program: results_list}
        return result 

    


def print_result(output_terminal):
    #printing the results
    cabecalho = ""
    title_ini = 'Name TOTAL KM Skip'
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
            elif ((i==0)and(len(v)==3)):
                print(v +'     ', end="")
            elif ((i==1)and(len(v)==1)):
                print(v +'      ', end="")
            elif ((i==1)and(len(v)==2)):
                print(v +'     ', end="")
            elif ((i==1)and(len(v)==3)):
                print(v +'    ', end="")
            elif ((i==2)and(len(v)==1)):
                print(v, end="")
            elif ((i==2)and(len(v)==5)):
                print(v[-5], end="")

            i+=1
        print('\n')
  
    

if __name__ == "__main__":

    #target dir
    sections_cosmic_ray = 'sections_cosmic_ray'
    database_cosmic_ray = 'database_cosmic_ray'
    sections_cosmic_ray_dir_begin = ROOT_DIR + '/sections_cosmic_ray'

    #check if the database dir exists and create if its nedded 
    d = ROOT_DIR + '/' + database_cosmic_ray
   
    try:
        os.stat(d)
    except:
        os.mkdir(d)  

    #store the results
    result_dict = {}

    #run for a single program
    if len(sys.argv) == 2:
        #read the program name
        python_program = str(sys.argv[1])
        python_program = python_program[:-3]
        string_result = run_a_program(sections_cosmic_ray,database_cosmic_ray,python_program)
        result_dict = process_output(string_result,python_program)
        print_result(result_dict)
    #run for all programs
    else:
        #walk into the dirs of the project
        for dir_name, subdir_list, file_list in os.walk(ROOT_DIR):

            #will run only on sections_cosmic_ray_dir_begin
            if dir_name == sections_cosmic_ray_dir_begin:

                #check every file into the dir    
                for python_program in file_list:
                    
                    #run the task if it's a toml file
                    if python_program[-4:] == 'toml':
                        python_program = python_program[:-5]
                        #execute cosmic ray and get the results
                        string_result = run_a_program(sections_cosmic_ray,database_cosmic_ray,python_program)
                        results = process_output(string_result, python_program)

                        #add the results in the final dictionary
                        result_dict.update(results) 
        #after get all the results, print in the screen
        print_result(result_dict)
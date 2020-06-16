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
    

    #split the results into a list
    results_list  = after.split()

    #get the target data
    total      = results_list[-9]
    killed     = results_list[-7]
    timeout    = results_list[-5]
    suspicious = results_list[-3]
    alive      = results_list[-1] 

    #update results_list with target data
    results_list = [total, killed, timeout, suspicious, alive]

    result = {program: results_list}

    return result 



def print_results(result_dict):

    #printing the results
    print('Name\t\t\t\t\t\tME/TM    MM     TL    Susp   SobV')
    print('-----------------------------------------------------------------------------------')
        
    for (key, values) in result_dict.items():
        #key is the name of the program
        #values are the results of the mutation testing
        
        print('{}\t\t\t\t\t'.format(key), end="  ")
        
        for v in values:
            print(v + '\t ', end="")
        
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
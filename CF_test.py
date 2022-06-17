import requests
from bs4 import BeautifulSoup
from subprocess import run, PIPE
import argparse

allInputs = []
allOutputs = []
plainInputs = []
plainOutputs = []
results = []
returnCodes = []

parser = argparse.ArgumentParser(description='This tool automates the test cases in a given problem from '
                                             'codeforces\n')

parser.add_argument('code_path', type=str,
                    help='Path of the c++ code')

parser.add_argument('problem', type=str,
                    help='Problem code , ex: 677/A')
args = parser.parse_args()


def compile_code(path):
    p = run(['g++', path, '-o',
             path.replace('.cpp', '')], stderr=PIPE)

    if p.returncode == 0:
        print('Compiled Successfully')
    else:
        print('Compilation Error IDIOT!')
        exit(-1)


def run_code(path):
    for i in range(len(allInputs)):
        p = run([path.replace('.cpp', '')], stdout=PIPE,
                input=plainInputs[i], encoding='ascii')
        returnCodes.append(p.returncode)
        results.append(p.stdout)


def print_result():
    if returnCodes.count(0) == len(returnCodes) and results == plainOutputs:
        print('Accepted, you are a Super HERO <3')
    else:
        print('Failed, you are a Big Dump IDIOT!!!!!!')


def print_detailed_result():
    for i in range(len(allInputs)):
        r = None
        if returnCodes[i] == 0 and results[i] == plainOutputs[i]:
            r = 'Passed'
        else:
            r = 'Failed'

        print(
            'Test Number {} {}, Input : {} , Expected : {} , Result : {}'.format(i + 1, r, plainInputs[i],
                                                                                 plainOutputs[i],
                                                                                 results[i]))


def parsing(html):
    global allInputs
    global allOutputs
    if html.status_code != 200:
        print('Please Provide a valid problem!')
        exit(1)
    cont = html.content
    soup = BeautifulSoup(cont, 'lxml')

    sample_test = soup.find('div', {'class': 'sample-test'})

    allInputs = sample_test.find_all('div', {'class': 'input'})
    allOutputs = sample_test.find_all('div', {'class': 'output'})

    if len(allInputs) != len(allOutputs):
        print('Length of extracted inputs not equal to length of extracted outputs from the website !')
        exit(-1)

    for i in range(len(allInputs)):
        plainInputs.append(allInputs[i].find('pre').get_text('<br>').replace('<br>', ' '))
        plainOutputs.append(allOutputs[i].find('pre').get_text('<br>').replace('<br>', ' '))


html = requests.get('https://codeforces.com/problemset/problem/' + args.problem)

parsing(html)
compile_code(args.code_path)
run_code(args.code_path)
print_result()
print_detailed_result()

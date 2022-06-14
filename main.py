# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import argparse
from io import TextIOWrapper
from zipfile import ZipFile
from colorama import Fore
from datetime import datetime

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #parser
    my_parser=argparse.ArgumentParser()
    my_parser.add_argument('function',
                           action='store',
                           choices=['sort','search','filter','count'],
                           help='set the function to use on zip file')
    my_parser.add_argument('arg_of_function',
                           action='store',
                           default='NULL')
    my_parser.add_argument('-additional_data_first',
                           action='store',
                           help='data by wich you filter')
    my_parser.add_argument('-additional_data_second',
                           action='store',
                           help='data by wich you filter')
    args=my_parser.parse_args()
    function=args.function

    #reading from the zip file
    with ZipFile('myFile0.zip') as zf:
        with zf.open('myFile0.csv', 'r') as data:
            reader = csv.reader(TextIOWrapper(data, 'utf-8'))
            header = next(reader)
            rows = []
            row = []
            for row in reader:
                rows.append(row)
    # functions to do
    if function == 'sort':
        col = args.arg_of_function
        result=sorted(rows,key=lambda row: row[int(col)-1])
        for i in range(0, 10):
            print('\n'+ str(result[i]))

    if function == 'search':
        word = args.arg_of_function
        k=0
        for line in rows:
            if word in str(line):
                if k<10:
                    print('\n' + str(line).replace(word, '{}{}{}'.format(Fore.YELLOW,word,Fore.RESET)))
                    k=k+1
                else:
                    break
        if k==0:
            print('word is not in the list')
    if function =='filter':
        col=args.arg_of_function
        col=int(col)-1
        k=0
        first_date=datetime.strptime(args.additional_data_first,"%d/%m/%Y")
        second_date=datetime.strptime(args.additional_data_second,"%d/%m/%Y")
        for line in rows:
            if col==5 and k<10:
                if first_date<datetime.strptime(line[col],"%d-%m-%Y")<second_date:
                    print(line)
                    k=k+1
            else:
                if col==8 and k<10:
                    if first_date < datetime.strptime(line[col], "%Y-%m-%d") < second_date:
                        line[col]=datetime.strptime(line[col], "%Y-%m-%d").strftime('%d-%m-%Y')
                        print(line)
                        k=k+1

    if function =='count':
        counter=0
        wrd_cnt=args.arg_of_function
        for line in rows:
            for subline in line:
                if wrd_cnt in subline:
                    counter+=1
        print(counter)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

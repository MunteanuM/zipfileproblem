# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import argparse
from io import TextIOWrapper
from zipfile import ZipFile
from colorama import Fore
from datetime import datetime


class Functionality:
    def __init__(self, function, arg_of_function, additional_data_first, additional_data_second, rows):
        self.function = function
        self.arg_of_function = arg_of_function
        self.additional_data_first = additional_data_first
        self.additional_data_second = additional_data_second
        self.rows = rows

    def result_of_function(self):
        if self.function == 'sort':
            col = self.arg_of_function
            result = sorted(self.rows, key=lambda row: row[int(col) - 1])
            for i in range(0, 10):
                print('\n' + str(result[i]))

        if self.function == 'search':
            word = self.arg_of_function
            limit_display = 0
            for line in self.rows:
                if word in str(line):
                    if limit_display < 10:
                        print('\n' + str(line).replace(word, '{}{}{}'.format(Fore.YELLOW, word, Fore.RESET)))
                        limit_display = limit_display + 1
                    else:
                        break
            if limit_display == 0:
                print('word is not in the list')
        if self.function == 'filter':
            col = self.arg_of_function
            col = int(col) - 1
            limit_display = 0
            first_date = datetime.strptime(self.additional_data_first, "%d/%m/%Y")
            second_date = datetime.strptime(self.additional_data_second, "%d/%m/%Y")
            for line in self.rows:
                if col == 5 and limit_display < 10:
                    if first_date < datetime.strptime(line[col], "%d-%m-%Y") < second_date:
                        print(line)
                        limit_display = limit_display + 1
                elif col == 8 and limit_display < 10:
                    if first_date < datetime.strptime(line[col], "%Y-%m-%d") < second_date:
                        line[col] = datetime.strptime(line[col], "%Y-%m-%d").strftime('%d-%m-%Y')
                        print(line)
                        limit_display = limit_display + 1

        if self.function == 'count':
            counter = 0
            searched_word = self.arg_of_function
            for line in self.rows:
                for subline in line:
                    if searched_word in subline:
                        counter += 1
            print(counter)


class Parser:
    def __init__(self):
        # parser
        my_parser = argparse.ArgumentParser()
        my_parser.add_argument('function',
                               action='store',
                               choices=['sort', 'search', 'filter', 'count'],
                               help='set the function to use on zip file')
        my_parser.add_argument('arg_of_function',
                               action='store',
                               default='NULL')
        my_parser.add_argument('-additional_data_first',
                               action='store',
                               help='data by which you filter',
                               default='01/01/2001')
        my_parser.add_argument('-additional_data_second',
                               action='store',
                               help='data by which you filter',
                               default='01/01/2001')
        self.args = my_parser.parse_args()


class ZipReader:
    def __init__(self, filenamezip, filenamecsv):
        self.filenamezip = filenamezip
        self.filenamecsv = filenamecsv
        with ZipFile(filenamezip) as zf:
            with zf.open(filenamecsv, 'r') as data:
                reader = csv.reader(TextIOWrapper(data, 'utf-8'))
                header = next(reader)
                self.rows = []
                for row in reader:
                    self.rows.append(row)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # parser
    args = Parser().args

    # reading from the zip file
    read_data = ZipReader('myFile0.zip', 'myFile0.csv').rows
    # the object that outputs the results of function
    operations_object = Functionality(args.function, args.arg_of_function, args.additional_data_first,
                                      args.additional_data_second, read_data)
    operations_object.result_of_function()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

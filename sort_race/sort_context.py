#
# creating functions for sort benchmark

import random
import string
import datetime


class DataSorter:
    data = []
    n = 3

    def get_random_letters_list(self, data_file_name="data.txt"):
        print("* get data")
        st_time = datetime.datetime.now().timestamp()
        try:
            with open(
                data_file_name, "r", encoding="utf-8", errors="replace"
            ) as c_file:
                # read data from file
                for c_line in c_file:
                    self.data.append(c_line)
        except IOError as e:
            print("File read IO_Error " + str(e))
            print("Generate new data set.")
            try:
                with open(
                    data_file_name, "w", encoding="utf-8", errors="replace"
                ) as c_file:
                    # creating data and write it to file
                    letters = string.ascii_lowercase
                    for _ in range(1_000_000):
                        random_string = ""
                        for _ in range(30):
                            random_string += random.choice(letters)
                        self.data.append(random_string)
                        c_file.write(random_string + "\n")
            except IOError as e:
                print("File write IO_Error " + str(e))
        print(f"* {str(len(self.data))} items")
        fin_time = datetime.datetime.now().timestamp()
        print("get_data_Time =", fin_time - st_time, "\n")

    def MyFn(self, s):
        return s

    def sorter(self, data):
        for i in range(1, self.n + 1):
            data_copy = data.copy()
            print(len(data_copy), end=" _ ")
            st = datetime.datetime.now().timestamp()
            data_copy.sort()
            fin = datetime.datetime.now().timestamp()
            print("Ss" + str(i), str(fin - st))

    def sorter_MyFn(self, data):
        for i in range(1, self.n + 1):
            data_copy = data.copy()
            print(len(data_copy), end=" _ ")
            st = datetime.datetime.now().timestamp()
            data_copy.sort(key=self.MyFn)
            fin = datetime.datetime.now().timestamp()
            print("Ms" + str(i), str(fin - st))

    def sorter_MyFn_reverse(self, data):
        for i in range(1, self.n + 1):
            data_copy = data.copy()
            print(len(data_copy), end=" _ ")
            st = datetime.datetime.now().timestamp()
            data_copy.sort(key=self.MyFn, reverse=True)
            fin = datetime.datetime.now().timestamp()
            print("Mr" + str(i), str(fin - st))

#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# multiprocessing.Pool version

import concurrent.futures
import random
import string
import datetime

data_file_name = "data.txt"
data = []
n = 3


def get_random_letters_list(data_file_name):
    global data
    print("* ft_Pool")
    st_time = datetime.datetime.now().timestamp()
    try:
        with open(data_file_name, "r", encoding="utf-8", errors="replace") as c_file:
            # read data from file
            for c_line in c_file:
                data.append(c_line)
    except IOError as e:
        print("File read IO_Error " + str(e))
        print("Generate new data set.")
        try:
            with open(
                data_file_name, "w", encoding="utf-8", errors="replace"
            ) as c_file:
                # if data not exists — create it and save copy to file
                letters = string.ascii_lowercase
                for _ in range(1_000_000):
                    random_string = ""
                    for _ in range(30):
                        random_string += random.choice(letters)
                    data.append(random_string)
                    c_file.write(random_string + "\n")
        except IOError as e:
            print("File write IO_Error " + str(e))
    fin_time = datetime.datetime.now().timestamp()
    print("letters_list_Time = " + str(fin_time - st_time))


def MyFn(s):
    return s


def sorter(data, i):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort()
    fin = datetime.datetime.now().timestamp()
    print("Ss" + str(i), str(fin - st), "_", len(data_copy))


def sorter_MyFn(data, i):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn)
    fin = datetime.datetime.now().timestamp()
    print("Ms" + str(i), str(fin - st), "_", len(data_copy))


def sorter_MyFn_reverse(data, i):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn, reverse=True)
    fin = datetime.datetime.now().timestamp()
    print("Mr" + str(i), str(fin - st), "_", len(data_copy))


# 9 executors x 1 task inside each
def future_pool_main():
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [sorter, sorter_MyFn, sorter_MyFn_reverse]
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for sl in sorters_list:
            for i in range(1, n + 1):
                executor.submit(sl, data, i)
    fin_time = datetime.datetime.now().timestamp()
    print("x\nft_Pool_9_SortTime = " + str(fin_time - st_time))


if __name__ == "__main__":
    st_time = datetime.datetime.now().timestamp()
    get_random_letters_list(data_file_name)
    future_pool_main()
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_9_OverallTime = " + str(fin_time - st_time))

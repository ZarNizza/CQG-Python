#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# multiprocessing.Process version

import random
import string
import datetime
from multiprocessing import Process, set_start_method

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


def sorter(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort()
    fin = datetime.datetime.now().timestamp()
    print("ss" + str(n) + "_" + str(fin - st))
    # return "ss" + str(n) + "_" + str(fin - st)


def sorter_MyFn(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn)
    fin = datetime.datetime.now().timestamp()
    print("Ms" + str(n) + "_" + str(fin - st))
    # return "Ms" + str(n) + "_" + str(fin - st)


def sorter_MyFn_reverse(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn, reverse=True)
    fin = datetime.datetime.now().timestamp()
    print("Mr" + str(n) + "_" + str(fin - st))
    # return "Mr" + str(n) + "_" + str(fin - st)


# 9 Process tasks
def proc_main():
    st_time = datetime.datetime.now().timestamp()
    set_start_method("spawn")
    p01 = Process(target=sorter, args=(data, 1))
    p02 = Process(target=sorter, args=(data, 2))
    p03 = Process(target=sorter, args=(data, 3))
    p11 = Process(target=sorter_MyFn, args=(data, 1))
    p12 = Process(target=sorter_MyFn, args=(data, 2))
    p13 = Process(target=sorter_MyFn, args=(data, 3))
    p21 = Process(target=sorter_MyFn_reverse, args=(data, 1))
    p22 = Process(target=sorter_MyFn_reverse, args=(data, 2))
    p23 = Process(target=sorter_MyFn_reverse, args=(data, 3))
    p01.start()
    p02.start()
    p03.start()
    p11.start()
    p12.start()
    p13.start()
    p21.start()
    p22.start()
    p23.start()
    p01.join()
    p02.join()
    p03.join()
    p11.join()
    p12.join()
    p13.join()
    p21.join()
    p22.join()
    p23.join()
    p01.terminate()
    p02.terminate()
    p03.terminate()
    p11.terminate()
    p12.terminate()
    p13.terminate()
    p21.terminate()
    p22.terminate()
    p23.terminate()
    fin_time = datetime.datetime.now().timestamp()
    print("x\nmp_Process_SortTime = " + str(fin_time - st_time))


if __name__ == "__main__":
    st_time = datetime.datetime.now().timestamp()
    get_random_letters_list(data_file_name)
    proc_main()
    fin_time = datetime.datetime.now().timestamp()
    print("mp_Process_OverallTime = " + str(fin_time - st_time))

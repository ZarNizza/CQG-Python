#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# asyncio version

import asyncio
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


async def a_sorter(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort()
    await asyncio.sleep(0)
    fin = datetime.datetime.now().timestamp()
    return "ss" + str(n) + "_" + str(fin - st)


async def a_sorter_MyFn(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn)
    await asyncio.sleep(0)
    fin = datetime.datetime.now().timestamp()
    return "Ms" + str(n) + "_" + str(fin - st)


async def a_sorter_MyFn_reverse(data, n=1):
    data_copy = data.copy()
    st = datetime.datetime.now().timestamp()
    data_copy.sort(key=MyFn, reverse=True)
    await asyncio.sleep(0)
    fin = datetime.datetime.now().timestamp()
    return "Mr" + str(n) + "_" + str(fin - st)


# async 9 tasks
async def a_main():
    st_time = datetime.datetime.now().timestamp()
    # Schedule three calls *concurrently*:
    q = await asyncio.gather(
        a_sorter(data, 1),
        a_sorter(data, 2),
        a_sorter(data, 3),
        a_sorter_MyFn(data, 1),
        a_sorter_MyFn(data, 2),
        a_sorter_MyFn(data, 3),
        a_sorter_MyFn_reverse(data, 1),
        a_sorter_MyFn_reverse(data, 2),
        a_sorter_MyFn_reverse(data, 3),
    )
    print(*q, sep="\n")
    fin_time = datetime.datetime.now().timestamp()
    print("asyncio_SortTime = " + str(fin_time - st_time))


st_time = datetime.datetime.now().timestamp()
get_random_letters_list(data_file_name)
asyncio.run(a_main())
fin_time = datetime.datetime.now().timestamp()
print("asyncio_OverallTime = " + str(fin_time - st_time))

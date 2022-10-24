#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# multiprocessing.Pool version

import concurrent.futures
import datetime
from sort_context import DataSorter

data_file_name = "data.txt"


# 3 executors x N tasks inside each
def sort_by_future_pool(self):
    print("* * * ft_Pool_Sort")
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [
        self.sorter,
        self.sorter_MyFn,
        self.sorter_MyFn_reverse,
    ]
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for sl in sorters_list:
            executor.submit(sl, self.data)
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_SortTime = " + str(fin_time - st_time))


# 3 executors (with .map) x N tasks inside each
def sort_by_future_pool_map(self):
    print("* * * ft_Pool_Sort with .map()")
    st_time = datetime.datetime.now().timestamp()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
        executor.map(self.sorter, self.data)
        # executor.map(self.sorter_MyFn, self.data)
        # executor.map(self.sorter_MyFn_reverse, self.data)
        executor.shutdown()
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_SortTime = " + str(fin_time - st_time))


if __name__ == "__main__":
    st_time = datetime.datetime.now().timestamp()
    ds = DataSorter()
    ds.get_random_letters_list(data_file_name)
    setattr(DataSorter, "sort_by_future_pool", sort_by_future_pool)
    ds.sort_by_future_pool()
    # setattr(DataSorter, "sort_by_future_pool_map", sort_by_future_pool_map)
    # ds.sort_by_future_pool_map()
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_OverallTime = " + str(fin_time - st_time))

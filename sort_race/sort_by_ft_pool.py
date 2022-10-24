#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# multiprocessing.Pool version

import concurrent.futures
import datetime
from sort_context import DataSorter

data_file_name = "data.txt"


# 3 executors x 3 jobs inside each
def sort_by_future_pool_main(self):
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [
        self.sorter,
        self.sorter_MyFn,
        self.sorter_MyFn_reverse,
    ]
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for sl in sorters_list:
            executor.submit(sl, self.data)
            # executor.map(sl, data)
            #
            # executor.map(sorter, data.copy())
            # executor.map(sorter_MyFn, data.copy())
            # executor.map(sorter_MyFn_reverse, data.copy())
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_SortTime = " + str(fin_time - st_time))


if __name__ == "__main__":
    print("ft_Pool_Sort")
    st_time = datetime.datetime.now().timestamp()
    ds = DataSorter()
    ds.get_random_letters_list(data_file_name)
    setattr(DataSorter, "sort_by_future_pool_main", sort_by_future_pool_main)
    ds.sort_by_future_pool_main()
    fin_time = datetime.datetime.now().timestamp()
    print("ft_Pool_OverallTime = " + str(fin_time - st_time))

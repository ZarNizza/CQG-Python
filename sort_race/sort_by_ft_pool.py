#
# Measure the execution time of a group of identical sorts
# in different versions of multithreading and asynchrony
#
# concurrent.futures.ProcessPoolExecutor version
# note: .map() creates one future per each data item — 1 000 000 in this study case )))


import concurrent.futures
import datetime
from sort_context import DataSorter

data_file_name = "data.txt"


# 3 executors x N tasks inside each
def sort_by_future_pool(self):
    print("* * * ft_ProcPoolExec_Sort")
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [
        self.sorter,
        self.sorter_MyFn,
        self.sorter_MyFn_reverse,
    ]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for sl in sorters_list:
            executor.submit(sl, self.data)
    fin_time = datetime.datetime.now().timestamp()
    print("ft_ProcPoolExec_SortTime = " + str(fin_time - st_time))


if __name__ == "__main__":
    ds = DataSorter()
    ds.get_random_letters_list(data_file_name)
    setattr(DataSorter, "sort_by_future_pool", sort_by_future_pool)
    ds.sort_by_future_pool()

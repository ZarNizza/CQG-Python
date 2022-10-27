'''Measure the execution time of a group of identical sorts
in different versions of multithreading and asynchrony

all-in-one version
note: .map() creates one future per each data item, = 1 000 000 in this study case )))
'''

import asyncio
import multiprocessing
import concurrent.futures
import datetime
from sort_context import DataSorter


def linear_sort(self):
    ''' linear execution
        3N serial tasks
    '''
    print("* * * linear_Sort")
    st_time = datetime.datetime.now().timestamp()
    self.batch_sorter(self.data)
    self.batch_sorter_MyFn(self.data)
    self.batch_sorter_MyFn_reverse(self.data)
    fin_time = datetime.datetime.now().timestamp()
    print("linear_overall_time = " + str(fin_time - st_time) + "\n")


def sort_by_future_pool(self):
    ''' concurrent.futures.ProcessPoolExecutor
        3 executors x N tasks inside each
    '''
    print("* * * ft_ProcPoolExec_Sort")
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [
        self.batch_sorter,
        self.batch_sorter_MyFn,
        self.batch_sorter_MyFn_reverse,
    ]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for sl in sorters_list:
            executor.submit(sl, self.data)
    fin_time = datetime.datetime.now().timestamp()
    print("ft_ProcPoolExec_overall_time = " + str(fin_time - st_time) + "\n")


def sort_by_future_pool_3n(self):
    ''' concurrent.futures.ProcessPoolExecutor
        3N executors x 1 task
    '''
    print("* * * 3N_ft_ProcPoolExec_Sort")
    st_time = datetime.datetime.now().timestamp()
    sorters_list = [
        self.sorter,
        self.sorter_MyFn,
        self.sorter_MyFn_reverse,
    ]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for sl in sorters_list:
            for i in range(1, 4):
                executor.submit(sl, self.data, i)
    fin_time = datetime.datetime.now().timestamp()
    print("3N_ft_ProcPoolExec_overall_time = " + str(fin_time - st_time) + "\n")


def sort_by_mp_pool(self):
    ''' multiprocessing.Pool
        3 async tasks x 3 tasks inside each
    '''
    print("* * * mp_Pool_Sort")
    st_time = datetime.datetime.now().timestamp()
    with multiprocessing.Pool() as pool:
        pool.apply_async(self.batch_sorter, (self.data,)).get()
        pool.apply_async(self.batch_sorter_MyFn, (self.data,)).get()
        pool.apply_async(self.batch_sorter_MyFn_reverse, (self.data,)).get()
    fin_time = datetime.datetime.now().timestamp()
    print("mp_Pool_overall_time = " + str(fin_time - st_time) + "\n")


def sort_by_mp_process(self):
    '''9 Process tasks
    '''
    print("* * * mp_Process_Sort")
    st_time = datetime.datetime.now().timestamp()
    # multiprocessing.set_start_method("spawn")
    p01 = multiprocessing.Process(target=self.sorter, args=(self.data, 1))
    p02 = multiprocessing.Process(target=self.sorter, args=(self.data, 2))
    p03 = multiprocessing.Process(target=self.sorter, args=(self.data, 3))
    p11 = multiprocessing.Process(target=self.sorter_MyFn, args=(self.data, 1))
    p12 = multiprocessing.Process(target=self.sorter_MyFn, args=(self.data, 2))
    p13 = multiprocessing.Process(target=self.sorter_MyFn, args=(self.data, 3))
    p21 = multiprocessing.Process(target=self.sorter_MyFn_reverse, args=(self.data, 1))
    p22 = multiprocessing.Process(target=self.sorter_MyFn_reverse, args=(self.data, 2))
    p23 = multiprocessing.Process(target=self.sorter_MyFn_reverse, args=(self.data, 3))
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
    print("mp_Process_overall_time = " + str(fin_time - st_time) + "\n")

async def async_sort(self):
    ''' async
        3N tasks *concurrently*
    '''
    print("* * * asyncio_Sort")
    st_time = datetime.datetime.now().timestamp()
    await asyncio.gather( self.async_sorter(self.data, 1),
        self.async_sorter(self.data, 2),   self.async_sorter(self.data, 3),
        self.async_sorter_MyFn(self.data, 1),
        self.async_sorter_MyFn(self.data, 2),
        self.async_sorter_MyFn(self.data, 3),
        self.async_sorter_MyFn_reverse(self.data, 1),
        self.async_sorter_MyFn_reverse(self.data, 2),
        self.async_sorter_MyFn_reverse(self.data, 3),
    )
    fin_time = datetime.datetime.now().timestamp()
    print("asyncio_overall_time = " + str(fin_time - st_time) + "\n")


if __name__ == "__main__":
    ds = DataSorter()
    ds.get_random_letters_list()

    setattr(DataSorter, "linear_sort", linear_sort)
    ds.linear_sort()
    setattr(DataSorter, "sort_by_future_pool", sort_by_future_pool)
    ds.sort_by_future_pool()
    setattr(DataSorter, "sort_by_future_pool_3n", sort_by_future_pool_3n)
    ds.sort_by_future_pool_3n()
    setattr(DataSorter, "sort_by_mp_pool", sort_by_mp_pool)
    ds.sort_by_mp_pool()
    setattr(DataSorter, "sort_by_mp_process", sort_by_mp_process)
    ds.sort_by_mp_process()
    setattr(DataSorter, "async_sort", async_sort)
    asyncio.run(ds.async_sort())

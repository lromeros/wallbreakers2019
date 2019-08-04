import math
import random
import threading


class MergeSortThread(threading.Thread):
    list_i = 0
    _list = []

    def __init__(self, list_i):
        self.list_i = list_i
        threading.Thread.__init__(self)

    def run(self):
        lock.acquire()
        self._list = merge_sort_thread(self.list_i)
        lock.release()


def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        elif i < len(left):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    return merged


def merge_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    half = math.ceil(len(num_list) / 2)
    left = merge_sort(num_list[:half])
    right = merge_sort(num_list[half:])

    return merge(left, right)


def merge_sort_thread(list_i):
    left_i = SUBLIST_SIZE * list_i
    half_i = left_i + math.ceil(SUBLIST_SIZE / 2)
    right_i = left_i + SUBLIST_SIZE

    left = merge_sort(NUMS[left_i:half_i])
    right = merge_sort(NUMS[half_i:right_i])
    list_i += 1

    return merge(left, right)


def split_into_n(nums, n):
    result = [[] for _ in range(n)]

    for i in range(len(nums)):
        bucket = i % n
        result[bucket].append(nums[i])

    return result


def list_of_size(list_size):
    _list = []

    for i in range(list_size):
        _list.append(random.randint(1, list_size))

    return _list


LIST_SIZE = 20
THREAD_NUM = 4
SUBLIST_SIZE = LIST_SIZE
thread_ctr = 0

lock = threading.Lock()
NUMS = list_of_size(LIST_SIZE)
print(f"Initial: {NUMS}")

sublists = split_into_n(NUMS, THREAD_NUM)
threads = []

for sublist in sublists:
    new_thread = MergeSortThread(thread_ctr)
    new_thread.start()
    threads.append(new_thread)

# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Sorted: {threads[0]._list}")
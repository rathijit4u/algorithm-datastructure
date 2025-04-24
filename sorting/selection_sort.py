import sys

def selection_sort(arr):
    arr_len = len(arr)
    for k in range(arr_len, 0, -1):
        max_idx = 0
        for i in range(1, k):
            if arr[max_idx] < arr[i]:
                max_idx = i
        if max_idx != k - 1:
            temp = arr[max_idx]
            arr[max_idx] = arr[k - 1]
            arr[k - 1] = temp


def selection_sort_recursive(arr, arr_len):
    if arr_len <= 1:
        return
    else:
        max_idx = 0
        for i in range(1, arr_len):
            if arr[i] > arr[max_idx]:
                max_idx = i
        temp = arr[max_idx]
        arr[max_idx] = arr[arr_len - 1]
        arr[arr_len - 1] = temp
        selection_sort_recursive(arr, arr_len - 1)


def display(arr):
    print(f"Before sorting: {arr}")
    selection_sort(arr)
    print(f"After sorting: {arr}")
    print("==================================")


def test_sort(arr):
    original_arr = arr.copy()
    display(arr)
    assert arr == sorted(original_arr)


if __name__ == "__main__":
    new_arr = [5, 4, 3, 2, 1]
    selection_sort_recursive(new_arr, len(new_arr))
    print(new_arr)
    print(sys.getrecursionlimit())

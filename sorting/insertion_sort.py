def insertion_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len - 1):
        key = i+1
        while (key - 1) >= 0 and arr[key] < arr[key-1]:
            arr[key], arr[key-1] = arr[key-1], arr[key]
            key -= 1


def display(arr):
    print(f"Before sorting: {arr}")
    insertion_sort(arr)
    print(f"After sorting: {arr}")
    print("==================================")


def test_sort(arr):
    original_arr = arr.copy()
    display(arr)
    assert arr == sorted(original_arr)

if __name__ == '__main__':
    new_arr = [9, 4, 1, 6, 8, 5, 3, 2, 7, 0]
    display(new_arr)
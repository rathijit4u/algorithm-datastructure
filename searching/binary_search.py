def binary_search(arr, search_term):
    arr_len = len(arr)
    if arr_len == 0:
        return False
    elif arr_len == 1:
        return arr[0] == search_term
    else:
        mid_idx = int((arr_len / 2)) + (arr_len % 2) - 1
        if arr[mid_idx] == search_term:
            return True
        elif arr[mid_idx] > search_term:
            return binary_search(arr[:mid_idx], search_term)
        else:
            return binary_search(arr[mid_idx+1:], search_term)

if __name__ == "__main__":
    print(binary_search([1,2,3,4,5,6,7,8,9], 9))
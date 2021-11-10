def dice_sum_helper(num_of_dice, sum_num, result):
    if num_of_dice == 0:
        if sum_num == 0:
            print(result)
    else:
        for i in range(1, 7):
            if i > sum_num:
                # print("Stopped execution. 'num_of_dice' = {0}, 'sum_num' = {1}, result = {2}, 'i' = {3}".format(
                # num_of_dice, sum_num, result, i))
                break
            result.append(i)
            remaining = sum_num - i
            dice_sum_helper(num_of_dice - 1, remaining, result)  # Explore
            result.pop()


def dice_sum(num_of_dice, sum_num):
    dice_sum_helper(num_of_dice, sum_num, [])


if __name__ == '__main__':
    dice_sum(3, 7)

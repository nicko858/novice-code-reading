from random import sample


def find_target_index(list_, target):
    if target in list_:
        return list_.index(target)


def generate_random_list(list_len, start, stop, step):
    return sorted(sample(range(start, stop, step), list_len))


if __name__ == "__main__":
    list_len = 10
    start, stop = 0, 101
    step = 2
    random_digits_set = generate_random_list(list_len, start, stop, step)

    try:
        target_digit = int(input('Pick a number between 0-100: '))
        target_index = find_target_index(random_digits_set, target_digit)

        print(f'List: {random_digits_set}')
        if target_index:
            print(f'Found {target_digit} in index {target_index}')
        else:
            print(f'Cannot find {target_digit} in the list')
    except ValueError:
        print('Invalid input')

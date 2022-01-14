from random import randint
import time


def generate():
    sequence = []
    for i in range(0, 11):
        sequence.append(str(randint(0, 9)))
    return "".join(sequence)


def get_digit(remain):
    return 0 if remain == 0 or remain == 1 else 11 - remain


def validate(cpf):
    is_valid = False
    
    # step one
    main_part = cpf[:9]
    digits = cpf[9:]
    controller = 10
    calc_list = []

    for index in range(0, len(main_part)):
        calc_list.append(int(main_part[index]) * controller)
        controller = controller - 1

    remain = sum(calc_list) % 11
    is_valid = get_digit(remain=remain) == int(digits[0])

    if not is_valid:
        return False
    
    # step two
    main_part = cpf[:10]
    controller = 11
    calc_list = []

    for index in range(0, len(main_part)):
        calc_list.append(int(main_part[index]) * controller)
        controller = controller - 1

    remain = sum(calc_list) % 11
    is_valid = get_digit(remain=remain) == int(digits[1])

    return is_valid


if __name__ == "__main__":
    start_time = time.time()
    
    valid_cpfs = set()
    
    number_of_cpfs = 5000
    #29 sec to generate 100k valid CPFs
    #300 sec 1M (5min)

    while len(valid_cpfs) < number_of_cpfs:
        number = generate()
        is_valid = validate(number)
        if is_valid:
            valid_cpfs.add(number)

    print("--- %s seconds ---" % (time.time() - start_time))
    print(len(valid_cpfs))

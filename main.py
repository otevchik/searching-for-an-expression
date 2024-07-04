target = 200

def find(answer, array, str):
    if not array:
        if (answer == target):
            return str
        return None

    number = array[0]
    array2 = array[1:]

    # subtraction
    if str:
        str_add = f"{str}-{number}"
    else:
        str_add = f"{number}"
    result = find(answer - number, array2, str_add)
    if result:
        return result

    # addition
    if str:
        str_add = f"{str}+{number}"
    else:
        str_add = f"{number}"
    result = find(answer + number, array2, str_add)
    if result:
        return result

    # empty
    if str:
        str_add = f"{str}{number}"
        answer2 = eval(str_add)
    else:
        str_add = f"{number}"
        answer2 = number
    result = find(answer2, array2, str_add)
    if result:
        return result

    return None

def main():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    str = ""
    answer = 0
    result = find(answer, array, str)

    if result:
        print(f"Результат: {result} = {target}")
    else:
        print("Не найдено такого примера")

if __name__ == "__main__":
    main()
target = 200
results = []

def find(answer, array, line):
    if not array:
        if (answer == target):
            if line not in results:
                results.append(line)
        return None

    number = array[0]
    array2 = array[1:]

    # subtraction
    if line:
        str_add = f"{line}-{number}"
    else:
        str_add = f"{number}"
    result = find(answer - number, array2, str_add)


    # addition
    if line:
        str_add = f"{line}+{number}"
    else:
        str_add = f"{number}"
    result = find(answer + number, array2, str_add)

    # empty
    if line:
        str_add = f"{line}{number}"
        answer2 = eval(str_add)
    else:
        str_add = f"{number}"
        answer2 = number
    result = find(answer2, array2, str_add)


    return results

def main():
    array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    line = ""
    answer = 0
    result = find(answer, array, line)

    if result:
        print("Результаты: ")
        for i in result:
            print(i)
    else:
        print("Не найдено такого примера")

if __name__ == "__main__":
    main()
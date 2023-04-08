def sum_two_numbers(left_number: int | float = 0,
                    right_number: int  | float = 0) -> int | float:
    """Сложить два числа, результат вывести в терминал и вернуть.
    
    Args:
        `left_number`: первое слагаемое, дефолтное значение `0`
        `right_number`: второе слагаемое, дефолтное значение `0`
    
    Returns:
        всегда возвращается число - сумма `left_number` и `right_number`
    """
    result = left_number + right_number
    print(left_number, '+', right_number, '=', result)
    return result


sum_two_numbers()
sum_two_numbers(left_number=5)
sum_two_numbers(right_number=8)
sum_two_numbers(5, 8)
sum_two_numbers(right_number=5, left_number=8)

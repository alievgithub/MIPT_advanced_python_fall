def DecoratedEvenNums(EvenNums):

    def wrapper(lst):

        if EvenNums(lst) == 0:
            return('Нет')
        elif EvenNums(lst) > 10:
            return('Очень много')
        else:
            return EvenNums(lst)

    return wrapper


def EvenNums(lst):
    length = 0;
    for x in lst:
        if x % 2 == 0:
            length += 1
    return length

Nums = list(map(int, input().split()))
print('Без декоратора', EvenNums(Nums))
EvenNumsNew = DecoratedEvenNums(EvenNums)
print('С декоратором', EvenNumsNew(Nums))

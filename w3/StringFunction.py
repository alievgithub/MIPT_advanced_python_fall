def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    function = lambda line: line + '\n'
    array = map(function, array)
    file_name.writelines(array)
    pass


with open('2.txt', 'w', encoding = 'utf8') as file:
    write_array(["What's", 'Up', '?!'], file)

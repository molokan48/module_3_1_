calls = int(0)
list_to_search = input('ввод списка через пробелы: ' ).split()
string = str(input('ввод строки: '))

list_to_search_up = [s.upper() for s in list_to_search]

def string_info ():
    count_calls()
    return tuple((len(string) , string.upper() , string.lower() ))


def is_contains ():
    count_calls()
    return string.upper() in list_to_search_up

def count_calls ():
    global calls
    calls = calls + 1

print('string_info: ' , string_info())
print('is_contains: ' , is_contains())
print('calls: ' , calls)
print('list_to_search:  ' , len(list_to_search) , ' elements')

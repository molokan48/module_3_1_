calls = int(0)
list_to_search = input('ввод списка через пробелы: ' ).split()
string = str(input('ввод строки: '))

list_to_search_up = [s.upper() for s in list_to_search]

def string_info ():
    print('string_info' , tuple((len(string) , string.upper() , string.lower() )))
    count_calls()

def is_contains ():
    print(string.upper() in list_to_search_up)
    count_calls()

def count_calls ():
    global calls
    calls = calls + 1

string_info()
is_contains()

print('calls: ' , calls)
print('list_to_search:  ' , len(list_to_search) , ' elements')
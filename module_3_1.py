# Создаем переменную calls для подсчета вызовов
calls = 0

#Функция для подсчета вызовов остальных функций
def count_calls():
    global calls
    calls += 1

# Функция для работы со строкой
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

# Функция для проверки наличия строки в списке
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

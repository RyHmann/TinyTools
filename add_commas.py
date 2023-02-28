import pyperclip


def get_clipboard():
    clipboard = pyperclip.paste()
    return clipboard


def clean_numbers(input_string):
    number_list = input_string.split()
    cleaned_numbers = []
    for number in number_list:
        cleaned_numbers.append(number.strip(','))
    return cleaned_numbers


def print_data(number_list):
    counter = 0
    for number in number_list:
        counter += 1
        if counter < len(number_list):
            print(f'{number},')
        else:
            print(f'{number}')


def insert_into_clipboard(number_list):
    counter = 0
    numbers = ''
    for number in number_list:
        counter += 1
        if counter < len(number_list):
            numbers += f'{number},\r'
        else:
            numbers += f'{number}'
    pyperclip.copy(numbers)


if __name__ == '__main__':
    clipboard_data = get_clipboard()
    clipboard_list = clean_numbers(clipboard_data)
    print_data(clipboard_list)
    insert_into_clipboard(clipboard_list)

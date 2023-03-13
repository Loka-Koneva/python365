import openpyxl

from faker_data import gen_fake_data


def example():
    """
    Создание файла и запись в него
    """
    book = openpyxl.Workbook()
    book.remove(book.active)

    book.create_sheet('Коллеги')
    book.create_sheet('Клиенты')
    book.create_sheet('Черный список', 0)

    for sheet in book.worksheets:
        for row in gen_fake_data():
            sheet.append(row)

    book.save('text.xlsx')

example()

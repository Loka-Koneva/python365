import openpyxl

def example():
    filename = 'text.xlsx'
    book = openpyxl.load_workbook(filename=filename)

    sheet: worksheet = book.worksheets[0]
    # Вставляем строку (также можно и колонки вставлять)
    sheet.insert_rows(0)

    sheet['A1'] = 'Name'
    sheet['B1'] = 'Phone'
    sheet['C1'] = 'Many'

    # Удаление и смещение данных вправо


    book.save(filename)

example()
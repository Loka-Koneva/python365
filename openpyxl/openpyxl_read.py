import openpyxl


def example():
    book = openpyxl.load_workbook(filename='text.xlsx')

    # Разные способы обращения к вкладкам
    # sheet = book.active
    # sheet = book.worksheet[1]
    sheet = book['Коллеги']

    # Первый способ чтения
    # for row in sheet.values:
    #     for cell in row:
    #         print(cell)

    # второй способ чтения
    # for row in sheet:
    #     for cell in row:
    #         print(cell.value)
    #         print(cell.font)

    for row in sheet.iter_rows():
        for cell in row:
            print(cell.value)


example()

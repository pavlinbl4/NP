from openpyxl.utils import get_column_letter


def set_column_dimensions(worksheet, columns_width):
    for column_number, column_width in enumerate(columns_width, start=1):
        worksheet.column_dimensions[f'{get_column_letter(3)}'].width = column_width

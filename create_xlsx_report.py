"""
проверя скачанные парсером снимки нового проспекта за месяц и генерю
файл отчета с превью
"""

from openpyxl import Workbook
from openpyxl.drawing.image import Image
import os
from datetime import datetime
from folder_in_MY_documents import make_documets_folder
from openpyxl.styles import (
    Border, Side,
    Alignment, Font
)

filename_data = datetime.now().day
month_name = datetime.now().month
current_year = datetime.now().year

way_to_files = f"{make_documets_folder('NewProspect')}/{current_year}_{month_name}"  # путь к папке с изображениями
# names = os.listdir(way_to_files)
names = os.listdir(way_to_files)

wb = Workbook()
ws = wb.active
ws.title = "Sheet with image"  # задаю название вкладки
ws.column_dimensions['C'].width = 40
ws.column_dimensions['A'].width = 20
ws.column_dimensions['B'].width = 95
ws.column_dimensions['D'].width = 20

count = 0
thin = Side(border_style="thin", color="000000")
for name in names:
    if name.endswith('JPG') or name.endswith('jpg'):
        count += 1
        ws.row_dimensions[count].height = 150  # задаю высоту столбца
        print(f"{way_to_files}/{name}")
        img = Image(f"{way_to_files}/{name}")
        resize_height = img.height // 3  # уменьшая рарешение в два раза
        resize_width = img.width // 3  # уменьшая рарешение в два раза

        img.width = resize_width  # устанавливаю размер превью
        img.height = resize_height  # устанавливаю размер превью
        ws[f'C{count}'].border = Border(left=thin, right=thin, top=thin,
                                        bottom=thin)
        ws.add_image(img, f'C{count}')

        ws[f'A{count}'].font = Font(size=14, bold=True)
        ws[f'A{count}'].alignment = Alignment(vertical='center')
        ws[f'A{count}'].border = Border(left=thin, right=thin, top=thin,
                                        bottom=thin)
        ws[f'A{count}'] = name.split("__")[0]

        ws[f'B{count}'].font = Font(size=12, bold=True)
        ws[f'B{count}'].alignment = Alignment(wrap_text=True, vertical='center')
        ws[f'B{count}'].border = Border(left=thin, right=thin, top=thin,
                                        bottom=thin)
        ws[f'B{count}'] = name.split("__")[1][:-4]

        ws[f'D{count}'].alignment = Alignment(horizontal='center', vertical='center')
        ws[f'D{count}'].border = Border(left=thin, right=thin, top=thin,
                                        bottom=thin)
        ws[f'D{count}'].font = Font(size=14, bold=True)
        ws[f'D{count}'] = 500

ws[f'D{count + 3}'].alignment = Alignment(horizontal='center', vertical='center')
ws[f'D{count + 3}'].font = Font(size=17, bold=True, color="FF0000")
ws[f'D{count + 3}'] = f"=SUM(D$1:D${count})"

ws[f'B{count + 3}'].font = Font(size=17, bold=True, color="FF0000")
ws[f'B{count + 3}'].alignment = Alignment(horizontal='center', vertical='center')
ws[f'B{count + 3}'] = "ИТОГО"

wb.save(f"{way_to_files}/report_{current_year}_{month_name}.xlsx")

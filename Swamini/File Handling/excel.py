import openpyxl

def write_content_to_file(filename, sheet_name, cell_name, cell_value):
    wb = openpyxl.Workbook()
    sheet_obj = wb.active
    cell = sheet_obj[f'{cell_name}']
    cell.value = cell_value
    wb.save(filename)
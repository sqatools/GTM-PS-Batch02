import openpyxl


















##############################

def write_content_to_file_overwrite(filename,sheet_name,cell_name,cell_value):
    wb = openpyxl.load_workbook(filename)
    sheet_obj=wb.create_sheet(sheet_name)
    cell = sheet_obj[f'{cell_name}']
    cell.value=cell_value
    wb.save(filename)

write_content_to_file_overwrite("python1.xlsx","Sheet2","A2","Modi Ji")

for i in range(1,50):
    write_content_to_file_overwrite("python1.xlsx","Sheet2",f"A{i}",f"{535534+i}")
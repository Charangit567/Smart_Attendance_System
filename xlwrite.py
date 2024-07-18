# xlwrite.py
import xlsxwriter
import os

def output(filename, sheet_name, row, id, name, status):
    filepath = f"{filename}.xlsx"

    # If the file does not exist, create it and write headers
    if not os.path.isfile(filepath):
        workbook = xlsxwriter.Workbook(filepath)
        worksheet = workbook.add_worksheet(sheet_name)
        worksheet.write(0, 0, "Row")
        worksheet.write(0, 1, "ID")
        worksheet.write(0, 2, "Name")
        worksheet.write(0, 3, "Status")
        workbook.close()

    # Re-open the workbook to add new data
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet(sheet_name)

    # Write data in the next available row
    next_row = row  # Use the row number provided

    worksheet.write(next_row, 0, next_row)
    worksheet.write(next_row, 1, id)
    worksheet.write(next_row, 2, name)
    worksheet.write(next_row, 3, status)

    workbook.close()
    return filepath

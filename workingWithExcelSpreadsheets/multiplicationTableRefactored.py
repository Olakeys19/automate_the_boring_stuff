#! python3
# multiplication_table_maker.py
# Creates an NxN multiplication table in an Excel spreadsheet.

import sys
import openpyxl
from openpyxl.styles import Font, Alignment


def apply_header_style(cell):
    """
    Apply the formatting used for header cells.
    """
    cell.font = Font(bold=True, italic=True)
    cell.alignment = Alignment(
        horizontal="center",
        vertical="center"
    )


def create_multiplication_table(size):
    """
    Create an NxN multiplication table and save it to an Excel file.
    """
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Freeze the top row and first column so headers remain visible.
    sheet.freeze_panes = "B2"

    # Top-left corner label.
    sheet["A1"] = "x"
    apply_header_style(sheet["A1"])

    # Create row and column headers.
    for number in range(1, size + 1):
        row_header = sheet.cell(row=number + 1, column=1)
        row_header.value = number
        apply_header_style(row_header)

        column_header = sheet.cell(row=1, column=number + 1)
        column_header.value = number
        apply_header_style(column_header)

    # Fill the multiplication table.
    for row in range(1, size + 1):
        for column in range(1, size + 1):
            result_cell = sheet.cell(
                row=row + 1,
                column=column + 1
            )

            result_cell.value = row * column
            result_cell.alignment = Alignment(
                horizontal="center",
                vertical="center"
            )

    filename = f"multiplicationTable{size}x{size}.xlsx"
    workbook.save(filename)

    print(f"{filename} has been created in the current working directory.")


def get_table_size():
    """
    Get the table size from the command line or user input.
    """
    if len(sys.argv) >= 2:
        return int(sys.argv[1])

    return int(input("Enter a number: "))


def main():
    print(
        "This program creates an NxN multiplication table "
        "based on the number 'N' given."
    )

    size = get_table_size()
    create_multiplication_table(size)


if __name__ == "__main__":
    main()
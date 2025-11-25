import csv
import sys
import os
from pathlib import Path

def read_csv(path):
    """Read CSV and preserve embedded newlines in quoted fields."""

    with path.open(newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader]


def split_multiline_cells(rows):
    """
    For each row, split any cell containing newline characters (\n)
    into a list of lines.
    """
    return [[cell.split("\n") for cell in row] for row in rows]


def compute_column_widths(multiline_rows):
    """Compute maximum width of each column (longest line in each cell)."""
    num_cols = len(multiline_rows[0])
    widths = [0] * num_cols

    for row in multiline_rows:
        for i, cell_lines in enumerate(row):
            max_len = max(len(line) for line in cell_lines)
            widths[i] = max(widths[i], max_len)
    return widths


def separator(widths, char="-"):
    """Build table separator line."""
    return "+" + "+".join(char * (w + 2) for w in widths) + "+"


def get_grid_table(multiline_rows):

    tab_as_str = ""

    widths = compute_column_widths(multiline_rows)

    # Header separator
    tab_as_str += separator(widths, "-")
    tab_as_str += "\n"

    for row_index, row in enumerate(multiline_rows):
        # Determine tallest cell in this row
        height = max(len(cell) for cell in row)

        # Print row lines
        for line_index in range(height):
            line = "|"
            for col_index, cell_lines in enumerate(row):
                text = cell_lines[line_index] if line_index < len(cell_lines) else ""
                line += " " + text.replace("--", "—").ljust(widths[col_index]) + " |"
            # print(line)
            tab_as_str += line
            tab_as_str += "\n"

        # Separator after header and after each row
        if row_index == 0:
            # print(separator(widths, "="))
            tab_as_str += separator(widths, "=")
            tab_as_str += "\n"

        else:
            # print(separator(widths, "-"))
            tab_as_str += separator(widths, "-")
            tab_as_str += "\n"
    return tab_as_str


# --------------------------------------------------------------------
# Main script
# --------------------------------------------------------------------
def main():
    folders_to_treat = ["input_csv", "input_files_csv", "output_csv"]
    containing_folder = "docs/source/how_to_use_the_model"

    existing_elements = os.listdir(containing_folder)

    for x in folders_to_treat:
        newname = x + "_as_rst"
        if newname not in existing_elements:
            os.mkdir(containing_folder+"/"+newname)

        files_to_convert = os.listdir(containing_folder + "/" + x)
        for fn in files_to_convert:
            print("=============", fn, "=============")
            if fn.endswith(".csv"):
                fn_new = fn.split(".csv")[0]+".rst"
                with open(containing_folder + "/" + x + "_as_rst" + "/" + fn_new, "w", encoding="utf-8") as f:
                    rows = read_csv(Path(containing_folder + "/" + x + "/" + fn))
                    multiline_rows = split_multiline_cells(rows)
                    f.write(get_grid_table(multiline_rows))

if __name__ == "__main__":
    main()
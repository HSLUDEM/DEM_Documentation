import csv
import sys
import os
import textwrap
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

def split_too_long_cells(multiline_rows, maxlen = 40):
    res = []
    for i in range(len(multiline_rows)):
        
        newline = []

        mr = multiline_rows[i]
        
        for c in mr:
            lh = []
            for ele in c:
                wrapped = textwrap.wrap(ele, width = maxlen)
                if len(wrapped) > 0:
                    for wrappedele in wrapped:
                        lh.append(wrappedele)
                else:
                    lh.append("")

            newline.append(lh)
        res.append(newline)
    # print(res)
    return res

def compute_column_widths(multiline_rows):
    """Compute maximum width of each column (longest line in each cell)."""
    num_cols = len(multiline_rows[0])
    widths = [0] * num_cols

    for row in multiline_rows:
        for i in range(len(row)):
            valmax = max([len(x) for x in row[i]])
            if valmax > widths[i]:
                widths[i] = valmax
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

            if line_index < height-1:
                line = "|"
                for col_index, cell_lines in enumerate(row):
                    text = ""
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
                    max_length_cells = split_too_long_cells(multiline_rows, maxlen = 40)
                    f.write(get_grid_table(max_length_cells))

if __name__ == "__main__":
    main()
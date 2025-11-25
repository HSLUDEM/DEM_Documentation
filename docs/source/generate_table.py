import csv
import sys
from pathlib import Path


argv = sys.argv
CSV_FILE = Path(argv[1])

def read_csv(path):
    """Read CSV and preserve embedded newlines in quoted fields."""
    with path.open(newline='') as f:
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


def print_grid_table(multiline_rows):
    """Print the final grid table to stdout."""
    widths = compute_column_widths(multiline_rows)

    # Header separator
    print(separator(widths, "="))

    for row_index, row in enumerate(multiline_rows):
        # Determine tallest cell in this row
        height = max(len(cell) for cell in row)

        # Print row lines
        for line_index in range(height):
            line = "|"
            for col_index, cell_lines in enumerate(row):
                text = cell_lines[line_index] if line_index < len(cell_lines) else ""
                line += " " + text.ljust(widths[col_index]) + " |"
            print(line)

        # Separator after header and after each row
        if row_index == 0:
            print(separator(widths, "="))
        else:
            print(separator(widths, "-"))


# --------------------------------------------------------------------
# Main script
# --------------------------------------------------------------------
def main():
    if not CSV_FILE.exists():
        print(f"Error: CSV file not found: {CSV_FILE}", file=sys.stderr)
        sys.exit(1)

    rows = read_csv(CSV_FILE)
    multiline_rows = split_multiline_cells(rows)
    print_grid_table(multiline_rows)


if __name__ == "__main__":
    main()
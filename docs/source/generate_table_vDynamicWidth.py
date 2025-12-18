import csv
import os
import textwrap
import re
from pathlib import Path
from typing import List


def read_csv(path: Path) -> List[List[str]]:
    """Read CSV and preserve embedded newlines in quoted fields."""
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader]


def split_multiline_cells(rows: List[List[str]]) -> List[List[List[str]]]:
    """
    For each row, split any cell containing newline characters (\n)
    into a list of lines.
    """
    return [[cell.split("\n") for cell in row] for row in rows]


_BACKTICK_RE = re.compile(r"``.*?``")  # non-greedy, supports multiple spans per line


def wrap_preserving_backticked_expressions(text: str, width: int) -> List[str]:
    """
    Wrap text to `width`, but keep any substring wrapped in ``...`` on a single line.
    The backticked spans are temporarily replaced by placeholders (no spaces),
    wrapped, then restored. Restored lines may exceed `width` (intended), causing
    the column to widen accordingly.
    """
    expr_map = {}

    def repl(m: re.Match) -> str:
        key = f"@@EXPR_{len(expr_map)}@@"
        expr_map[key] = m.group(0)
        return key

    protected = _BACKTICK_RE.sub(repl, text)

    wrapped = textwrap.wrap(
        protected,
        width=width,
        break_long_words=True,
        break_on_hyphens=False,
    )

    out: List[str] = []
    for line in (wrapped if wrapped else [""]):
        for key, expr in expr_map.items():
            line = line.replace(key, expr)
        out.append(line)

    return out


def split_too_long_cells(multiline_rows: List[List[List[str]]], maxlen: int = 40) -> List[List[List[str]]]:
    """
    Wrap each line in each cell to `maxlen`, but keep ``...`` expressions unbroken.
    """
    res: List[List[List[str]]] = []
    for mr in multiline_rows:
        new_row: List[List[str]] = []
        for cell_lines in mr:
            lh: List[str] = []
            for ele in cell_lines:
                wrapped_lines = wrap_preserving_backticked_expressions(ele, width=maxlen)
                lh.extend(wrapped_lines if wrapped_lines else [""])
            new_row.append(lh)
        res.append(new_row)
    return res


def compute_column_widths(multiline_rows: List[List[List[str]]]) -> List[int]:
    """Compute maximum width of each column (longest line in each cell)."""
    if not multiline_rows:
        return []
    num_cols = len(multiline_rows[0])
    widths = [0] * num_cols

    for row in multiline_rows:
        for i in range(len(row)):
            cell_lines = row[i]
            valmax = max((len(x) for x in cell_lines), default=0)
            if valmax > widths[i]:
                widths[i] = valmax
    return widths


def separator(widths: List[int], char: str = "-") -> str:
    """Build table separator line."""
    return "+" + "+".join(char * (w + 2) for w in widths) + "+"


def get_grid_table(multiline_rows: List[List[List[str]]], notitleline: bool = False) -> str:
    tab_as_str = ""

    widths = compute_column_widths(multiline_rows)

    # Top separator
    tab_as_str += separator(widths, "-") + "\n"

    for row_index, row in enumerate(multiline_rows):
        # Determine tallest cell in this row
        height = max((len(cell) for cell in row), default=0)

        # Print row lines (with a blank spacer line between wrapped lines, as in your original)
        for line_index in range(height):
            line = "|"
            for col_index, cell_lines in enumerate(row):
                text = cell_lines[line_index] if line_index < len(cell_lines) else ""
                line += " " + text.replace("--", "—").ljust(widths[col_index]) + " |"
            tab_as_str += line + "\n"

            if line_index < height - 1:
                spacer = "|"
                for col_index, _cell_lines in enumerate(row):
                    spacer += " " + "".ljust(widths[col_index]) + " |"
                tab_as_str += spacer + "\n"

        # Separator after header and after each row
        if row_index == 0 and not notitleline:
            tab_as_str += separator(widths, "=") + "\n"
        else:
            tab_as_str += separator(widths, "-") + "\n"

    return tab_as_str


# --------------------------------------------------------------------
# Main script
# --------------------------------------------------------------------
def main() -> None:
    for notitleline in [True, False]:
        folders_to_treat = ["input_csv", "input_files_csv", "output_csv"]
        containing_folder = "how_to_use_the_model"

        existing_elements = os.listdir(containing_folder)

        for x in folders_to_treat:
            newname = x + "_as_rst"
            if newname not in existing_elements:
                os.mkdir(containing_folder + "/" + newname)

            files_to_convert = os.listdir(containing_folder + "/" + x)
            for fn in files_to_convert:
                print("=============", fn, "=============")
                if fn.endswith(".csv"):
                    fn_new = fn.split(".csv")[0] + ("_notitleline" if notitleline else "") + ".rst"
                    out_path = Path(containing_folder) / f"{x}_as_rst" / fn_new

                    rows = read_csv(Path(containing_folder) / x / fn)
                    multiline_rows = split_multiline_cells(rows)
                    max_length_cells = split_too_long_cells(multiline_rows, maxlen=40)

                    with out_path.open("w", encoding="utf-8") as f:
                        f.write(get_grid_table(max_length_cells, notitleline=notitleline))


if __name__ == "__main__":
    main()

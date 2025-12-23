# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 10:38:01 2025

@author: UeliSchilt
"""

import os
from pathlib import Path
import pandas as pd
from typing import Dict, List, Optional, Union

# Path to the feather file
file_path = (
    r"C:/Users/UeliSchilt/OneDrive - Hochschule Luzern/"
    r"02_Github_DEM_Doc/DEM_Data/data_all/master_data/"
    r"simulation_data/meta_file_2.feather"
)

# Folder where the .rst file will be saved
output_path = r"how_to_use_the_model/swiss_munic_table/"

# Keys = df columns, values = headers in rst table
column_allocation: Dict[str, str] = {
    "Municipality": "Municipality (``GGDENAME``)",
    "GGDENR": "Commune number (``GGDENR``)",
    "Canton": "Canton",
}

# Read the feather file
df = pd.read_feather(file_path)


def df_to_rst_list_table(
    df: pd.DataFrame,
    column_allocation: Dict[str, str],
    rst_file: Union[str, os.PathLike],
    title: Optional[str] = None,
    max_rows: Optional[int] = None,
) -> None:
    """
    Write selected DataFrame columns into a reStructuredText list-table.
    """

    requested_cols = list(column_allocation.keys())

    missing = [c for c in requested_cols if c not in df.columns]
    if missing:
        print(f"Warning: Missing columns skipped: {missing}")

    present_cols = [c for c in requested_cols if c in df.columns]
    if not present_cols:
        raise ValueError("None of the requested columns are present in the dataframe.")

    out_df = df.loc[:, present_cols].copy()

    if max_rows is not None:
        out_df = out_df.head(max_rows)

    # Bold headers
    headers = [f"**{column_allocation[c]}**" for c in present_cols]

    rst_file = Path(rst_file)
    rst_file.parent.mkdir(parents=True, exist_ok=True)

    lines: List[str] = []

    if title:
        lines.append(title)
        lines.append("=" * len(title))
        lines.append("")

    lines.append(".. list-table::")
    lines.append("   :header-rows: 1")
    lines.append("")

    # Header row
    lines.append(f"   * - {headers[0]}")
    for h in headers[1:]:
        lines.append(f"     - {h}")

    # Data rows
    for _, row in out_df.iterrows():
        values = ["" if pd.isna(row[c]) else str(row[c]) for c in present_cols]
        lines.append(f"   * - {values[0]}")
        for v in values[1:]:
            lines.append(f"     - {v}")

    lines.append("")

    rst_file.write_text("\n".join(lines), encoding="utf-8")


# Output file
rst_filename = "swiss_municipalities_table.rst"
rst_file_path = Path(output_path) / rst_filename

df_to_rst_list_table(
    df=df,
    column_allocation=column_allocation,
    rst_file=rst_file_path,
    title=None,
    max_rows=None,
)

print(f"RST table written to: {rst_file_path}")

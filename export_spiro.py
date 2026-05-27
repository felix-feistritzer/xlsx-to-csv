import pandas as pd
from datetime import datetime

# date is saved from 1900-01-01
# timestamp() function calculate from 1970-01-01
# this is the time difference in seconds (70 years)
date_offset = 2208988800

def time_to_seconds(dt, time_format=None):
    """Convert datetime or string to seconds since epoch."""
    if isinstance(dt, pd.Timestamp):
        return dt.timestamp() + date_offset
    seconds =  pd.to_datetime(dt, format=time_format).timestamp()
    return (seconds + date_offset)

def export_data_to_csv(
    input_file: str,
    output_file: str,
    data_column: str,
    start_time: str,
    end_time: str,
    skip_rows: int = 0,
    time_format: str = None,
):
    """
    Exports data from a specific column in an xlsx file to a CSV file,
    filtered by a time interval in the first column.

    Args:
        input_file: Path to the input xlsx file.
        output_file: Path to the output CSV file.
        data_column: Name or index of the column to export.
        start_time: Start time for filtering (inclusive).
        end_time: End time for filtering (inclusive).
        skip_rows: Number of rows to skip at the beginning.
        time_format: Format of the time column (e.g., "%Y-%m-%d %H:%M:%S").
                    If None, pandas will try to infer the format.
    """

    """
    xlsx file must be saved as a workbook!
    """

    # Read the xlsx file, skipping the specified rows
    df = pd.read_excel(input_file, skiprows=skip_rows)

    # Skip the second line (index 1) if it exists
    if len(df) > 0:
        df.drop(index=0, inplace=True)

    # Reset index after dropping a row
    df.reset_index(drop=True, inplace=True)

    # Ensure the first column is parsed as datetime
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format=time_format)

    # Filter rows based on the time interval
    mask = (df.iloc[:, 0] >= pd.to_datetime(start_time, format=time_format)) & (df.iloc[:, 0] <= pd.to_datetime(end_time, format=time_format))
    filtered_df = df.loc[mask]

    # Select the time and data columns
    result_df = filtered_df.iloc[:, [0, df.columns.get_loc(data_column)]]

    # Convert to seconds
    result_df.iloc[:, 0] = result_df.iloc[:, 0].apply(lambda x: time_to_seconds(x, time_format))

    # Save to CSV
    result_df.to_csv(output_file, index=False, header=False)

# Example usage:
# export_data_to_csv(
#     input_file="data.xlsx",
#     output_file="output.csv",
#     data_column="Temperature",
#     start_time="2023-01-01 00:00:00",
#     end_time="2023-01-31 23:59:59",
#     skip_rows=5,
#     time_format="%Y-%m-%d %H:%M:%S",
# )

export_data_to_csv(
    input_file="data/Prob_01_spiro_workbook.xlsx",
    output_file="out/Prob_01_spiro.csv",
    data_column="V'E",
    start_time="0:08:05",
    end_time="0:24:05",
    skip_rows=121,
    time_format="%H:%M:%S",
)

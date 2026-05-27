import pandas as pd

def export_data_to_csv(
    input_file: str,
    output_file: str,
    data_column: str,
    start_time: str,
    end_time: str,
    skip_rows: int = 0,
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
    """
    # Read the xlsx file, skipping the specified rows
    df = pd.read_excel(input_file, skiprows=skip_rows)

    # Filter rows based on the time interval
    mask = (df.iloc[:, 0] >= start_time) & (df.iloc[:, 0] <= end_time)
    filtered_df = df.loc[mask]

    # Select the time and data columns
    result_df = filtered_df.iloc[:, [0, df.columns.get_loc(data_column)]]

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
# )


export_data_to_csv(
    input_file="data/Prob_01.xlsx",
    output_file="out/Prob_01.csv",
    data_column=18,
    start_time=10195,
    end_time=19786,
    skip_rows=78,
)
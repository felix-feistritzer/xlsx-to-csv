# xlsx to csv

Exports data from a specific column in an xlsx file to a CSV file,
filtered by a time interval in the first column.

## NIRS

Example usage:

```
export_data_to_csv(
    input_file="data.xlsx",
    output_file="output.csv",
    data_column="Temperature",
    start_time="35",
    end_time="1080",
    skip_rows=5,
)
```

| Args | Description |
|---------|--------------|
| `input_file` | Path to the input xlsx file with NIRS data. |
| `output_file` | Path to the output CSV file. |
| `data_column` | Name or index of the column to export. |
| `start_time` | Start time for filtering (inclusive). |
| `end_time` | End time for filtering (inclusive). |
| `skip_rows` | Number of rows to skip at the beginning. |

## Spiro

```
Example usage:
export_data_to_csv(
    input_file="data.xlsx",
    output_file="output.csv",
    data_column="Temperature",
    start_time="0:08:05",
    end_time="0:24:05",
    skip_rows=5,
    time_format="%H:%M:%S",,
)
```

| Args | Description |
|---------|--------------|
| `input_file` | Path to the input xlsx file with NIRS data. |
| `output_file` | Path to the output CSV file. |
| `data_column` | Name or index of the column to export. |
| `start_time` | Start time for filtering (inclusive). |
| `end_time` | End time for filtering (inclusive). |
| `skip_rows` | Number of rows to skip at the beginning. |
| `time_format` | Format of the time column (e.g., "%Y-%m-%d %H:%M:%S"). If None, pandas will try to infer the format. |

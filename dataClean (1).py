# import pandas as pd
#
#
# def main() -> pd.DataFrame:
#     # Load the Excel file, skipping the first 14 rows
#     df = pd.read_excel("Project_H_Master Sheet Jan'23 to Dec'24 (1).xlsx",
#                        skiprows=14,
#                        header=[0, 1, 2, 3]
#                        )
#     df = df.reset_index(drop=True).iloc[:779]
#     df = df.reindex()
#
#     df1 = pd.melt(df, id_vars=[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')])
#     print("Columns in DataFrame:", df1.columns)
#     print("Shape of Melted DataFrame:", df1.shape)  # Debug point
#
#     # Return the melted dataframe
#     print(df1.head())
#     cleaned_df = df1.dropna(subset=['value'])
#     cleaned_df = cleaned_df[
#         (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Total") &
#         (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Date") &
#         (~pd.isna(cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')]))&
#         (cleaned_df['value'] != 0) &
#         (cleaned_df['value'] != "Total")
#         ]
#
#     #print(cleaned_df.head())
#     cleaned_df = cleaned_df.rename(columns={('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3'): "Date","variable_0": "Vehicle Type","variable_1": "Collection Type","variable_2": "Journey Type","variable_3": "Payment Type","value":"Volume"})
#     cleaned_df.to_csv("cleaned_output3.csv",index = False)
#     return cleaned_df
#
#
#
# if __name__ == "__main__":
#     # Run and inspect
#     main()




import pandas as pd

def filterByValue(file_path: str) -> pd.DataFrame:
    df = pd.read_excel(file_path, skiprows=14, header=[0, 1, 2, 3])
    df = df.reset_index(drop=True).iloc[782:,:200]
    df = df.reindex()

    # Melt the DataFrame
    df1 = pd.melt(df, id_vars=[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')])
    print("Columns in DataFrame:", df1.columns)
    print("Shape of Melted DataFrame:", df1.shape)  # Debug point

    # Display the melted dataframe
    print(df1.head())

    # Drop rows where 'value' is NaN
    cleaned_df = df1.dropna(subset=['value'])

    # Apply filtering conditions
    cleaned_df = cleaned_df[
                (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Total") &
                (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Date") &
                (~pd.isna(cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')]))&
                (cleaned_df['value'] != 0) &
                (cleaned_df['value'] != "Total")
                ]

    # Rename columns for better readability
    cleaned_df = cleaned_df.rename(columns={
        ('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3'): "Date",
        "variable_0": "Vehicle Type",
        "variable_1": "Collection Type",
        "variable_2": "Journey Type",
        "variable_3": "Payment Type",
        "value": "Value"
    })

    # Save the cleaned DataFrame to a CSV file
    #cleaned_df.to_csv("cleaned_output3.csv", index=False)
    return cleaned_df

def filterByVolume(file_path: str) -> pd.DataFrame:
    """
    This function reads the Excel file, applies cleaning and transformation steps,
    and returns the cleaned DataFrame.
    """
    # Load the Excel file, skipping the first 14 rows
    df = pd.read_excel(file_path, skiprows=14, header=[0, 1, 2, 3])
    df = df.reset_index(drop=True).iloc[:779,:200]
    df = df.reindex()

    # Melt the DataFrame
    df1 = pd.melt(df, id_vars=[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')])
    print("Columns in DataFrame:", df1.columns)
    print("Shape of Melted DataFrame:", df1.shape)  # Debug point

    # Display the melted dataframe
    print(df1.head())

    # Drop rows where 'value' is NaN
    cleaned_df = df1.dropna(subset=['value'])

    # Apply filtering conditions
    cleaned_df = cleaned_df[
                (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Total") &
                (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Date") &
                (~pd.isna(cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')]))&
                (cleaned_df['value'] != 0) &
                (cleaned_df['value'] != "Total")
                ]

    # Rename columns for better readability
    cleaned_df = cleaned_df.rename(columns={
        ('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3'): "Date",
        "variable_0": "Vehicle Type",
        "variable_1": "Collection Type",
        "variable_2": "Journey Type",
        "variable_3": "Payment Type",
        "value": "Volume"
    })

    # Save the cleaned DataFrame to a CSV file
    #cleaned_df.to_csv("cleaned_output_volume1.csv", index=False)
    return cleaned_df


def mergeDataFrames(file_path: str) -> pd.DataFrame:
    """
    This function merges the two DataFrames created by `filterByVolume` and `filterByValue` functions.
    """
    # Generate the two cleaned DataFrames
    df_volume = filterByVolume(file_path)
    df_value = filterByValue(file_path)

    # Merge the DataFrames on relevant column(s)
    # Assuming 'Date' is a common column to perform the merge
    merged_df = pd.merge(df_volume, df_value, on=["Date","Vehicle Type","Collection Type","Journey Type","Payment Type"], suffixes=('_volume', '_value'))

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv("merged_output3.csv", index=False)
    print("Merged DataFrame created successfully.")

    return merged_df


def main():
    # Define the file path (replace with your actual file path)
    file_path = "Project_H_Master Sheet Jan'23 to Dec'24 (1).xlsx"

    # # Call the function to merge both cleaned DataFrames
    # merged_df = mergeDataFrames(file_path)
    #
    # # Optionally display or further process the merged DataFrame
    # print("First few rows of the merged DataFrame:")
    # print(merged_df.head())
    mergeDataFrames(file_path)


if __name__ == "__main__":
    main()




# import pandas as pd
#
# def filterByValue(file_path: str) -> pd.DataFrame:
#     df = pd.read_excel(file_path, skiprows=14, header=[0, 1, 2, 3])
#     df = df.reset_index(drop=True).iloc[782:,:200]
#     df = df.reindex()
#
#     # Melt the DataFrame
#     df1 = pd.melt(df, id_vars=[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')])
#     print("Columns in DataFrame:", df1.columns)
#     print("Shape of Melted DataFrame:", df1.shape)  # Debug point
#
#     # Display the melted dataframe
#     print(df1.head())
#
#     # Drop rows where 'value' is NaN
#     cleaned_df = df1.dropna(subset=['value'])
#     print(cleaned_df.columns)
#     # Apply filtering conditions
#     # cleaned_df = cleaned_df[
#     #             (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Total") &
#     #             (cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')] != "Date") &
#     #             (~pd.isna(cleaned_df[('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3')]))&
#     #             (cleaned_df['value'] != 0) &
#     #             (cleaned_df['value'] != "Total")
#     #             ]
#
#     # Rename columns for better readability
#     cleaned_df = cleaned_df.rename(columns={
#         ('Date', 'Unnamed: 0_level_1', 'Unnamed: 0_level_2', 'Unnamed: 0_level_3'): "Date",
#         "variable_0": "Vehicle Type",
#         "variable_1": "Collection Type",
#         "variable_2": "Journey Type",
#         "variable_3": "Payment Type",
#         "value": "Value"
#     })
#
#     # Save the cleaned DataFrame to a CSV file
#     cleaned_df.to_csv("Demo_cleaned_output13.csv", index=False)
#     return cleaned_df
#
#
# def main():
#     # Define the file path (replace with your actual file path)
#     file_path = "Project_H_Master Sheet Jan'23 to Dec'24 (1).xlsx"
#     filterByValue(file_path)
#     # # Call the function to merge both cleaned DataFrames
#     # merged_df = mergeDataFrames(file_path)
#     #
#     # # Optionally display or further process the merged DataFrame
#     # print("First few rows of the merged DataFrame:")
#     # print(merged_df.head())
#     #mergeDataFrames(file_path)
#
#
# if __name__ == "__main__":
#     main()
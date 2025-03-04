import pandas as pd
def generate_monthly_reports(Financial_Sample):
    # Read the dataset from the Excel file
    df = pd.read_excel(D:\BI Projects Repository\BI-Projects\Monthly report from excel file/Financial Sample)

    # Ensure there's a 'Date' column to group by month
    if 'Date' not in df.columns:
        raise ValueError("The dataset must contain a 'Date' column.")
     # Convert the 'Date' column to datetime type
    df['Date'] = pd.to_datetime(df['Date'])

        # Add a 'Month' column for grouping
    df['Month'] = df['Date'].dt.to_period('M')

        # Group by the 'Month' column
    grouped = df.groupby('Month')
        
    for month, group in grouped:
        # Define the output file name
        Output_Data = f'report_{month}.xlsx'
        
     # Save each group's data to an Excel file
        group.to_excel(Output_Data, index=False)
        print(f'Report for {month} saved as {Output_Data}')

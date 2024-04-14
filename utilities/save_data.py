import csv
import os

def write_data_to_csv(current_script, time, data_folder_path, contract_address, data_rows):
    # Get the current script's filename without the directory path or file extension
    script_filename = os.path.basename(current_script).replace('.py', '')

    # Extract the descriptive name from the script name
    descriptive_name = script_filename.split('get_')[-1]

    # Create the directory structure
    base_folder = os.path.join(data_folder_path, time, descriptive_name)
    os.makedirs(base_folder, exist_ok=True)

    # Define the CSV file path
    csv_file_path = os.path.join(base_folder, f"{contract_address}.csv")

    # Write the data rows to the CSV file
    if data_rows:
        headers = data_rows[0].keys()
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data_rows)
    
    return csv_file_path


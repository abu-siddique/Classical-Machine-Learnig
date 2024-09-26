import os
import shutil
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_extract(dataset, file_name, download_path, extract_path):
    
    target_file_path = os.path.join(extract_path, file_name)
    
    # Check if the file already exists in the target directory
    if os.path.exists(target_file_path):
        print(f"{file_name} already exists in {extract_path}. Skipping download.")
        return
    
    
    api = KaggleApi()
    api.authenticate()
    
    # Download the dataset file
    api.dataset_download_file(dataset, file_name, path=download_path)
    
    zip_file_path = os.path.join(download_path, f"{file_name}.zip")
    csv_file_path = os.path.join(download_path, file_name)
    
    # Check if the zip file exists
    if os.path.exists(zip_file_path):
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(extract_path)
        # Clean up: Remove the ZIP file
        os.remove(zip_file_path)
    else:
        # Move the CSV file if the ZIP file is not present
        if os.path.exists(csv_file_path):
            shutil.move(csv_file_path, extract_path)
            
def download_and_extract_competition(competition, file_name, download_path, extract_path):
    # Ensure the directories exist
    os.makedirs(download_path, exist_ok=True)
    os.makedirs(extract_path, exist_ok=True)
    
    target_file_path = os.path.join(extract_path, file_name)
    
    # Check if the file already exists in the target directory
    if os.path.exists(target_file_path):
        print(f"{file_name} already exists in {extract_path}. Skipping download.")
        return
    
    api = KaggleApi()
    api.authenticate()
    
    try:
        # Download the competition dataset
        api.competition_download_file(competition, file_name, path=download_path)
        
        zip_file_path = os.path.join(download_path, f"{file_name}.zip")
        csv_file_path = os.path.join(download_path, file_name)
        
        # Check if the zip file exists
        if os.path.exists(zip_file_path):
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(extract_path)
            # Clean up: Remove the ZIP file
            os.remove(zip_file_path)
        else:
            # Move the CSV file if the ZIP file is not present
            if os.path.exists(csv_file_path):
                shutil.move(csv_file_path, extract_path)
    except Exception as e:
        print(f"An error occurred: {e}")

# Execute the function
download_and_extract_competition(competition="house-prices-advanced-regression-techniques", file_name="train.csv", download_path="./", extract_path="data/external/house-prices/")

# Execute the function
# download_and_extract(dataset="zynicide/wine-reviews", file_name="winemag-data-130k-v2.csv", download_path="./", extract_path="data/external/house-prices/")

import kaggle
import zipfile
import os

kaggle.api.authenticate()

kaggle.api.dataset_download_file(
    dataset="zynicide/wine-reviews",
    file_name="winemag-data-130k-v2.csv",
    path="./",
)

with zipfile.ZipFile("winemag-data-130k-v2.csv.zip", "r") as zip_ref:
    zip_ref.extractall("data/external/wine-reviews/")

# Clean up: Remove the ZIP file
os.remove("winemag-data-130k-v2.csv.zip")

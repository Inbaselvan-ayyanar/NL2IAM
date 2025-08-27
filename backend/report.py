import csv
import os

STORAGE_DIR = r"C:/Users/ainba/Downloads/aws frontend/my-react-vite-app/backend"

def update_data(data, type):
    # Ensure backend directory exists
    os.makedirs(STORAGE_DIR, exist_ok=True)

    # Full file path
    file_path = os.path.join(STORAGE_DIR, f"{type}.csv")

    # Append data safely
    with open(file_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)



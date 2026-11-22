import csv
import shutil
import hashlib
from pathlib import Path
from datetime import datetime

# Project directory
BASE_DIR = Path(__file__).resolve().parent

# Source sensor data
SOURCE_FILE = BASE_DIR / "sensor_readings.csv"

# Backup directory
BACKUP_DIR = BASE_DIR / "backups"


def calculate_checksum(file_path):
    """Calculate SHA-256 checksum of a file."""
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def create_backup():
    print("\n===== SECURE IOT DATA BACKUP =====")

    if not SOURCE_FILE.exists():
        print("Error: sensor_readings.csv not found.")
        print("Run iot_sensor.py first.")
        return

    if SOURCE_FILE.stat().st_size == 0:
        print("Error: Sensor data file is empty.")
        return

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_file = BACKUP_DIR / f"sensor_backup_{timestamp}.csv"

    try:
        shutil.copy2(SOURCE_FILE, backup_file)

        checksum = calculate_checksum(backup_file)

        print("Backup created successfully!")
        print(f"Backup file: {backup_file.name}")
        print(f"File size: {backup_file.stat().st_size} bytes")
        print(f"SHA-256: {checksum}")

    except OSError as error:
        print(f"Backup failed: {error}")


if __name__ == "__main__":
    create_backup()
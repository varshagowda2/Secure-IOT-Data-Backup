import os
import csv
import random
import time
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from supabase import create_client

# ------------------------------------------------
# 1. LOAD SUPABASE CONFIGURATION
# ------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)

SUPABASE_URL = os.getenv("https://rrfelxysrwmyqwgdrqmd.supabase.co")
SUPABASE_KEY = os.getenv("sb_publishable_maJOHdx_2oH_MarcYxx4aQ_jIGfXyWI")

TABLE_NAME = "sensor_readings"

# ------------------------------------------------
# 2. CONNECT TO SUPABASE
# ------------------------------------------------

supabase = None

if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        print("Supabase connection initialized successfully!")

    except Exception as error:
        print("Supabase connection failed:", error)

else:
    print("Supabase credentials not found.")
    print("Sensor data will be saved locally only.")

# ------------------------------------------------
# 3. IOT SENSOR CONFIGURATION
# ------------------------------------------------

DEVICE_ID = "SENSOR001"
LOCATION = "Bengaluru"
TOTAL_READINGS = 5

readings = []

# ------------------------------------------------
# 4. GENERATE SENSOR DATA
# ------------------------------------------------

print("\n===================================")
print("   SECURE IOT DATA BACKUP SYSTEM")
print("===================================")

print("\nStarting IoT sensor simulation...\n")

for number in range(1, TOTAL_READINGS + 1):

    temperature = round(random.uniform(24, 35), 2)
    humidity = round(random.uniform(40, 80), 2)

    reading = {
        "device_id": DEVICE_ID,
        "temperature": temperature,
        "humidity": humidity,
        "location": LOCATION,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    readings.append(reading)

    print(f"Reading {number}:")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"Location: {LOCATION}")
    print("-----------------------------------")

    time.sleep(1)

# ------------------------------------------------
# 5. SAVE SENSOR DATA TO CSV
# ------------------------------------------------

csv_file = BASE_DIR / "sensor_readings.csv"

try:
    with open(csv_file, "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "device_id",
            "temperature",
            "humidity",
            "location",
            "timestamp"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(readings)

    print("\nSensor data saved to CSV successfully!")
    print("File:", csv_file.name)

except OSError as error:
    print("CSV saving failed:", error)

# ------------------------------------------------
# 6. UPLOAD DATA TO SUPABASE
# ------------------------------------------------

if supabase is not None:

    try:
        response = (
            supabase
            .table(TABLE_NAME)
            .insert(readings)
            .execute()
        )

        print("\nData uploaded to Supabase successfully!")
        print("Total records uploaded:", len(readings))

    except Exception as error:
        print("\nSupabase upload failed!")
        print("Error:", error)

else:
    print("\nSupabase upload skipped.")
    print("Please configure your .env credentials.")

# ------------------------------------------------
# 7. COMPLETION MESSAGE
# ------------------------------------------------

print("\n===================================")
print("   IOT SENSOR SIMULATION COMPLETED")
print("===================================")
import os
from pathlib import Path
from supabase import create_client

print("\n====================================")
print("       SUPABASE DATA UPLOAD")
print("====================================")

# Locate the project directory
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

# Check whether .env exists
if not ENV_FILE.exists():
    raise FileNotFoundError("ERROR: .env file not found!")

# Read .env directly
config = {}

with open(ENV_FILE, "r", encoding="utf-8-sig") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if "=" in line:
            key, value = line.split("=", 1)

            config[key.strip()] = (
                value.strip().strip('"').strip("'")
            )

# Get credentials
SUPABASE_URL = config.get("SUPABASE_URL", "")
SUPABASE_KEY = config.get("SUPABASE_KEY", "")
SUPABASE_BUCKET = config.get("SUPABASE_BUCKET", "")

# Display credential status
print("\nChecking Supabase credentials...")

print("ENV FILE EXISTS:", ENV_FILE.exists())
print("URL DETECTED:", bool(SUPABASE_URL))
print("KEY DETECTED:", bool(SUPABASE_KEY))
print("BUCKET DETECTED:", bool(SUPABASE_BUCKET))

# Validate credentials
if not all([
    SUPABASE_URL,
    SUPABASE_KEY,
    SUPABASE_BUCKET
]):
    raise ValueError(
        "Missing credentials. Correct your .env file."
    )

if not SUPABASE_URL.startswith("https://"):
    raise ValueError("Invalid Supabase URL.")

# Connect to Supabase
print("\nConnecting to Supabase...")

try:
    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

    print("Supabase client created successfully!")

except Exception as error:
    print("Connection error:", error)
    raise

# Locate CSV file
csv_files = list(BASE_DIR.glob("sensor_readings*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "ERROR: sensor_readings CSV file not found!"
    )

csv_file = csv_files[0]

print("\nCSV FOUND:", csv_file.name)

# Upload data
try:
    with open(csv_file, "rb") as file:
        file_data = file.read()

    result = supabase.storage.from_(
        SUPABASE_BUCKET
    ).upload(
        path=csv_file.name,
        file=file_data,
        file_options={
            "content-type": "text/csv",
            "upsert": "true"
        }
    )

    print("\n====================================")
    print("       UPLOAD SUCCESSFUL")
    print("====================================")
    print("File:", csv_file.name)
    print("Bucket:", SUPABASE_BUCKET)

except Exception as error:
    print("\nUPLOAD FAILED!")
    print("Reason:", error)
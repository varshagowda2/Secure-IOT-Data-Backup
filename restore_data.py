import os
from pathlib import Path
from dotenv import dotenv_values
from supabase import create_client

# Get the exact folder containing this Python file
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

print("=" * 50)
print("       SUPABASE DATA RESTORATION")
print("=" * 50)

# Read .env directly from the project folder
if not ENV_FILE.is_file():
    raise FileNotFoundError(
        f".env file not found at: {ENV_FILE}"
    )

env = dotenv_values(ENV_FILE)

# Read credentials and remove accidental spaces
SUPABASE_URL = (
    env.get("SUPABASE_URL")
    or os.getenv("SUPABASE_URL")
    or ""
).strip().strip('"').strip("'")

SUPABASE_KEY = (
    env.get("SUPABASE_KEY")
    or env.get("SUPABASE_SERVICE_ROLE_KEY")
    or os.getenv("SUPABASE_KEY")
    or os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    or ""
).strip().strip('"').strip("'")

SUPABASE_BUCKET = (
    env.get("SUPABASE_BUCKET")
    or "iot-backup-storage"
).strip().strip('"').strip("'")

print("\nChecking credentials...")
print("ENV FILE EXISTS:", ENV_FILE.is_file())
print("URL DETECTED:", bool(SUPABASE_URL))
print("KEY DETECTED:", bool(SUPABASE_KEY))
print("BUCKET DETECTED:", bool(SUPABASE_BUCKET))

try:
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError(
            "URL or KEY missing. Check the .env file."
        )

    print("\nConnecting to Supabase...")

    supabase = create_client(
        SUPABASE_URL,
        SUPABASE_KEY
    )

    print("Supabase connected successfully!")

    file_name = "sensor_readings.csv"

    print("\nDownloading:", file_name)

    response = supabase.storage.from_(
        SUPABASE_BUCKET
    ).download(file_name)

    output_file = BASE_DIR / "restored_sensor_readings.csv"

    with open(output_file, "wb") as file:
        file.write(response)

    print("\n" + "=" * 50)
    print("       RESTORATION SUCCESSFUL")
    print("=" * 50)

    print("Bucket:", SUPABASE_BUCKET)
    print("File:", file_name)
    print("Saved as:", output_file.name)
    print("File size:", len(response), "bytes")

except Exception as error:
    print("\nRESTORATION FAILED")
    print("Error:", error)
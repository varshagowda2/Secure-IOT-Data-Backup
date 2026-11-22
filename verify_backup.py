import hashlib
from pathlib import Path

print("=" * 45)
print("     BACKUP INTEGRITY VERIFICATION")
print("=" * 45)

original = Path("sensor_readings.csv")
restored = Path("restored_sensor_readings.csv")

if not original.exists():
    print("ERROR: Original CSV file not found.")
elif not restored.exists():
    print("ERROR: Restored CSV file not found.")
else:
    def get_hash(file):
        return hashlib.sha256(file.read_bytes()).hexdigest()

    original_hash = get_hash(original)
    restored_hash = get_hash(restored)

    print("\nOriginal file:", original.name)
    print("Restored file:", restored.name)

    print("\nOriginal SHA-256:", original_hash)
    print("Restored SHA-256:", restored_hash)

    if original_hash == restored_hash:
        print("\nSUCCESS: Data integrity verified!")
        print("Original and restored files are identical.")
    else:
        print("\nFAILED: Files are different.")

print("=" * 45)
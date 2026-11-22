# Secure IoT Data Backup and Restoration System

## Project Overview

The Secure IoT Data Backup and Restoration System is a Python-based project designed to securely store, back up, and restore IoT sensor data using Supabase Cloud Storage.

The system collects IoT sensor readings, stores them in CSV format, uploads backup files to Supabase, and restores the data whenever required. It also verifies data integrity using SHA-256 hashing to ensure that the restored file is identical to the original file.

## Objectives

- Collect IoT sensor data.
- Store sensor readings in CSV format.
- Create secure backups of sensor data.
- Upload backup files to Supabase Cloud Storage.
- Restore backup files from cloud storage.
- Verify restored data using SHA-256 hashing.
- Maintain data integrity and availability.

## Technologies Used

- Python
- Supabase
- Supabase Storage
- CSV
- SHA-256 Hashing
- Visual Studio Code
- Git and GitHub
- Python Virtual Environment

## Project Structure

```text
Secure_IOT_Data_Backup/
│
├── backups/
│   └── sensor_backup_*.csv
│
├── iot_sensor.py
├── backup_data.py
├── upload_data.py
├── restore_data.py
├── verify_backup.py
│
├── sensor_readings.csv
├── restored_sensor_readings.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Project Modules

### 1. IoT Sensor Data Generation

File: `iot_sensor.py`

Generates sample IoT sensor readings, including:
- Device ID
- Temperature
- Humidity
- Location
- Timestamp

### 2. Data Backup

File: `backup_data.py`

Creates backup copies of sensor readings and stores them locally in CSV format.

### 3. Cloud Upload

File: `upload_data.py`

Connects to Supabase and uploads the sensor backup file to the cloud storage bucket.

### 4. Data Restoration

File: `restore_data.py`

Downloads the backup file from Supabase Storage and saves it locally as:

`restored_sensor_readings.csv`

### 5. Backup Integrity Verification

File: `verify_backup.py`

Uses SHA-256 hashing to compare the original and restored files.

If both hash values match, the system confirms that the restored data is identical to the original data.

## Supabase Configuration

The project uses Supabase Storage for cloud backup.

Storage Bucket:

`iot-backup-storage`

Environment variables are stored in a local `.env` file.

Example configuration:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_secret_key
```

**Security Note:** Never upload your actual `.env` file or secret keys to GitHub.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/varshagowda2/Secure-IOT-Data-Backup.git
```

### Step 2: Open the Project Folder

```bash
cd Secure-IOT-Data-Backup
```

### Step 3: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 4: Activate Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Configure Environment Variables

Create a `.env` file in the project folder and add your Supabase credentials.

### Step 7: Run the Project

Run the Python files in the following order:

```bash
python iot_sensor.py
python backup_data.py
python upload_data.py
python restore_data.py
python verify_backup.py
```

## Data Integrity Verification

The system uses the SHA-256 algorithm to verify backup integrity.

Example successful output:

```text
BACKUP INTEGRITY VERIFICATION

Original file: sensor_readings.csv
Restored file: restored_sensor_readings.csv

Original SHA-256: [hash value]
Restored SHA-256: [hash value]

SUCCESS: Data integrity verified!
Original and restored files are identical.
```

## Project Result

The system successfully connects to Supabase, uploads IoT sensor backup data, downloads the stored backup, and restores the CSV file.

SHA-256 verification confirms that the original and restored files have identical hash values.

## Advantages

- Secure cloud-based data backup.
- Easy data restoration.
- Data integrity verification.
- Reduced risk of data loss.
- Organized storage of IoT sensor readings.
- Simple and efficient implementation.

## Conclusion

The Secure IoT Data Backup and Restoration System provides an efficient solution for backing up and restoring IoT sensor data using Python and Supabase Cloud Storage.

The SHA-256 verification mechanism ensures data integrity and confirms that the restored data matches the original data.

## Author

**Varshini M**

Project: Secure IoT Data Backup and Restoration System
## Project Screenshots

### 1. IoT Sensor Simulation
![IoT Sensor Simulation](screenshots/01_sensor_simulation.png)

### 2. Local Data Backup
![Local Backup](screenshots/02_backup_success.png)

### 3. Supabase Cloud Upload
![Supabase Upload](screenshots/03_supabase_upload.png)

### 4. Data Restoration
![Data Restoration](screenshots/04_data_restoration.png)

### 5. SHA-256 Integrity Verification
![Integrity Verification](screenshots/05_integrity_verification.png)

### 6. Supabase Storage
![Supabase Storage](screenshots/06_supabase_storage.png)

### 7. GitHub Repository
![GitHub Repository](screenshots/07_github_repository.png)
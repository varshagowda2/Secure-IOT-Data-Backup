Secure IoT Data Backup Using Python and Supabase

Project Overview

Secure IoT Data Backup is a cloud-based project developed using Python and Supabase. The project focuses on collecting IoT sensor data, securely uploading data to cloud storage, creating backups, and restoring stored data when required.

Objectives

- Collect IoT sensor data using Python.
- Upload data to Supabase cloud storage.
- Maintain secure data backups.
- Restore backed-up data when required.
- Demonstrate cloud computing and data management.

Technologies Used

- Programming Language: Python
- Cloud Platform: Supabase
- Database / Storage: Supabase
- Libraries: Supabase Python SDK, Python-dotenv
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub

Project Structure

Secure_IOT_Data_Backup/
│
├── backup_data.py
├── iot_sensor.py
├── upload_data.py
├── restore_data.py
├── requirements.txt
├── .gitignore
└── .env

Note: The ".env" file is stored locally and must never be uploaded to GitHub.

Main Features

1. IoT Sensor Data Collection: Collects sensor data using Python.
2. Data Backup: Creates backups of collected IoT data.
3. Cloud Upload: Uploads backup data to Supabase.
4. Data Restoration: Retrieves previously backed-up data.
5. Secure Configuration: Uses environment variables to protect credentials.

Installation and Setup

1. Clone the Repository

git clone https://github.com/varshagowda2/Secure-IOT-Data-Backup.git

2. Open the Project Folder

cd Secure-IOT-Data-Backup

3. Create a Virtual Environment

python -m venv .venv

4. Activate the Virtual Environment

For Windows:

.venv\Scripts\activate

5. Install Dependencies

pip install -r requirements.txt

6. Configure Environment Variables

Create a local ".env" file and add your Supabase configuration:

SUPABASE_URL=YOUR_PROJECT_URL
SUPABASE_KEY=YOUR_PUBLISHABLE_KEY
SUPABASE_EMAIL=YOUR_REGISTERED_EMAIL
SUPABASE_PASSWORD=YOUR_PASSWORD

Never share or upload actual credentials.

Running the Project

Run the Python scripts from the project folder according to their functionality:

python iot_sensor.py

python backup_data.py

python upload_data.py

python restore_data.py

Expected Outcome

The project demonstrates how IoT sensor data can be collected, backed up, uploaded to a cloud platform, and restored when needed.

Conclusion

Secure IoT Data Backup provides a practical demonstration of integrating Python with Supabase cloud services. It helps understand IoT data management, cloud storage, backup mechanisms, and data restoration.

Author

Varshini M

Project: Secure IoT Data Backup Using Python and Supabase

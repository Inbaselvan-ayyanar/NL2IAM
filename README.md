# 🚀 NL2IAM

---

## 📌 Overview
**NL2IAM** is a web-based tool that simplifies and automates the management of AWS **IAM Users** and **IAM Groups** by leveraging **natural language processing**. Administrators can interact with the system using plain English commands or upload CSV files containing user and group information. NL2IAM interprets these inputs to automatically create, update, and assign IAM resources in **AWS using boto3**, reducing manual effort and human error. The platform also generates detailed audit reports to track successful and failed operations, ensuring transparency, compliance, and efficient IAM governance across your AWS environment.


---

## ⚙️ Features
- ✅ **Natural Language Automation** – Manage IAM resources with plain English commands  
- ✅ **IAM Group Automation** – Create groups with inline policies  
- ✅ **IAM User Automation** – Create/update users with default login credentials  
- ✅ **User-to-Group Assignment** – Automatically assigns users to specified groups  
- ✅ **CSV File Upload** – Upload `data.csv` (groups) and `user_data.csv` (users)  
- ✅ **Audit Reports** – Generates `group_report.csv` and `user_report.csv`  
- ✅ **Web Interface** – Intuitive React frontend for managing automation  

---


## Prerequisites
- Python 3.9+

- Node.js & npm

- AWS credentials configured (~/.aws/credentials)

- IAM role with permissions:

  - iam:CreateUser

  - iam:CreateGroup

  - iam:PutGroupPolicy

  - iam:AddUserToGroup

  - iam:CreateLoginProfile

  - iam:UpdateLoginProfile

---

## Backend Setup

- cd backend
- pip install -r requirements.txt
- python flask_app.py   

--- 
## Frontend Setup

- cd frontend
- npm install
- npm run dev 

---

## 🚀 Future Enhancements

- ☁️ **Expand to Multiple Cloud Services** – Extend automation beyond AWS to services like S3, EC2, and more, enabling cross-cloud resource management.  
- 🤖 **Multiple Automation Types** – Automate not just IAM users and groups, but also storage provisioning, policy enforcement, and other cloud tasks using natural language commands.  
- 🗣️ **Voice & NLP Interaction** – Manage cloud resources using plain English or voice commands, making automation more intuitive and accessible.  
---

## ✍️ Author: Inbaselvan Ayyanar 
## Gmail : a.inbaselvan@gmail.com

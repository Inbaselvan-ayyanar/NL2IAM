import Json_structure
import pandas as pd
import boto3
from botocore.exceptions import ClientError
import json
import report
import os
STORAGE_DIR = r"C:/Users/ainba/Downloads/aws frontend/my-react-vite-app/backend"

# Make sure directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

def delete_files(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def create_aws_Group():
    
    file_path = os.path.join(STORAGE_DIR, "group_report.csv")
    delete_files(file_path)

    data_path = os.path.join(STORAGE_DIR, "data.csv")
    data = pd.read_csv(data_path, delimiter=',', quotechar='"', on_bad_lines='skip')

    for index,row in data.iterrows():
        print(index," ",row["GroupName"]," ",row["Description"])
        create_aws_user_Group_Boto(row["Description"],row["GroupName"])

   
    delete_files(data_path)

def create_aws_user():
    

    file_path = os.path.join(STORAGE_DIR, "user_report.csv")
    delete_files(file_path)

    data_path = os.path.join(STORAGE_DIR, "user_data.csv")

    data = pd.read_csv(data_path, delimiter=',', quotechar='"', on_bad_lines='skip')
    for index,row in data.iterrows():
        if row["GroupName"] != "NULL":
            print(index," ",row["userID"]," ",row["GroupName"])
            create_aws_user_Boto(row["userID"],row["GroupName"])
        else:
            print(index," ",row["userID"]," ",row["Group_Description"])

    
    delete_files(data_path)

def create_aws_user_Group_Boto(Description, groupName):
    iam = boto3.client('iam')

    inline_policy_name = groupName + 'Policy'
    policy_json = Json_structure.create_aws_group_Json_structure(Description)
    group_arn = None

    try:
        # Try creating the group
        response = iam.create_group(GroupName=groupName)
        group_arn = response['Group']['Arn']
        print(f"IAM Group '{groupName}' created successfully.")
        print("Group ARN:", group_arn)
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Group '{groupName}' already exists. Updating policy...")
        # Get ARN for existing group
        group_info = iam.get_group(GroupName=groupName)
        group_arn = group_info['Group']['Arn']

        # Remove old policy if it exists
        try:
            iam.delete_group_policy(GroupName=groupName, PolicyName=inline_policy_name)
            print(f"Old policy '{inline_policy_name}' removed from group '{groupName}'.")
        except iam.exceptions.NoSuchEntityException:
            print(f"No existing policy found for group '{groupName}'.")
    except Exception as e:
        report.update_data([groupName, Description, e, group_arn], "group_report")
        return

    # Attach the new policy
    iam.put_group_policy(
        GroupName=groupName,
        PolicyName=inline_policy_name,
        PolicyDocument=json.dumps(policy_json)
    )
    print(f"New inline policy '{inline_policy_name}' attached to group '{groupName}'.")

    # Save report with ARN
    report.update_data([groupName, Description, "Policy Updated/Created", group_arn], "group_report")


def create_aws_user_Boto(ID, groupName):
    iam = boto3.client('iam')
    user_name = ID
    password = 'Welcome*ToAWS'  # Make sure this meets your password policy
    user_arn = None

    # Check if the group exists
    try:
        iam.get_group(GroupName=groupName)
        print(f"Group '{groupName}' exists. Proceeding...")
    except iam.exceptions.NoSuchEntityException:
        print(f"Group '{groupName}' does not exist. Skipping user creation.")
        report.update_data([user_name, groupName, password, "User not created", None], "user_report")
        return  # Stop function here

    # Try creating the user
    try:
        response = iam.create_user(UserName=user_name)
        user_arn = response['User']['Arn']
        print(f"IAM User '{user_name}' created successfully.")
        print("User ARN:", user_arn)
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User '{user_name}' already exists. Adding to group if not already in it...")
        # Fetch ARN for existing user
        user_info = iam.get_user(UserName=user_name)
        user_arn = user_info['User']['Arn']

    # Add the user to the specified group
    try:
        iam.add_user_to_group(GroupName=groupName, UserName=user_name)
        print(f"IAM User '{user_name}' added to group '{groupName}' successfully.")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User '{user_name}' is already in group '{groupName}'.")

    # Create or update login profile
    try:
        iam.create_login_profile(
            UserName=user_name,
            Password=password,
            PasswordResetRequired=True
        )
        print(f"Login profile created for '{user_name}'.")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Login profile for '{user_name}' already exists. Updating...")
        iam.update_login_profile(
            UserName=user_name,
            Password=password,
            PasswordResetRequired=True
        )
        print(f"Login profile updated for '{user_name}'.")

    # Save report with ARN
    report.update_data(
        [user_name, groupName, password, "User Created/Updated", user_arn],
        "user_report"
    )




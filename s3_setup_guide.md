# AWS S3 Setup Instructions

## 1. Create S3 Bucket
1. Login to [AWS Console](https://console.aws.amazon.com/)
2. Go to Services → S3 → Create bucket
3. Enter a unique bucket name (e.g., codtech-intern-task1-yourname)
4. Choose region (e.g., Asia Pacific (Mumbai) - ap-south-1)
5. Uncheck "Block all public access" (for public access setup)
6. Acknowledge the warning and click "Create bucket"

## 2. Upload Example File
1. Click on the created bucket
2. Click **Upload**, add `example_file.txt`, and click **Upload**

## 3. Set Public Permissions (Read Access)
1. After upload, click on the file
2. Go to **Permissions** tab
3. Under **Object Ownership**, ensure it's set to "Bucket owner preferred"
4. Under **Public access**, click "Edit" → enable public read access

## 4. Test File Access
- Copy the **Object URL**
- Open in browser to verify public access

## 5. Optional: Automate Upload Using Python (Boto3)
Run `upload_script.py` to upload a file programmatically.

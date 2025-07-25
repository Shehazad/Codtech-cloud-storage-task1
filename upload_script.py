import boto3

# Replace with your details
bucket_name = 'codtech-intern-task1-yourname'
file_path = 'example_file.txt'
object_name = 'example_file.txt'

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file
s3.upload_file(file_path, bucket_name, object_name)

print(f'File {object_name} uploaded to {bucket_name} successfully.')

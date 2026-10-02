import os

from dotenv import load_dotenv

load_dotenv()
AWS_REGION = os.getenv("AWS_REGION")
AWS_ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
TC_APP_EC2 = os.getenv("TC_APP_EC2")
TC_RENDER_LAMBDA = os.getenv("TC_RENDER_LAMBDA")
TC_RENDER_S3 = os.getenv("TC_RENDER_S3")
TC_APP_EC2_INSTANCE_ID = os.getenv("TC_APP_EC2_INSTANCE_ID")

VERSION = "2012-10-17"

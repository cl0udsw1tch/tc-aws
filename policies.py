from config import AWS_ACCOUNT_ID, AWS_REGION, TC_APP_EC2_INSTANCE_ID

permission_policies = {
    "ssm:cmd:exec": {
        "Effect": "Allow",
        "Action": "ssm:SendCommand",
        "Resource": [
            f"arn:aws:ec2:{AWS_REGION}:{AWS_ACCOUNT_ID}:instance/{TC_APP_EC2_INSTANCE_ID}",
            f"arn:aws:ssm:{AWS_REGION}::document/AWS-RunShellScript",
        ],
    },
    "ssm:cmd:read": {
        "Effect": "Allow",
        "Action": ["ssm:GetCommandInvocation", "ssm:ListCommandInvocations"],
        "Resource": "*",
    },
    "ssm:cmd:deploy": {
        "Effect": "Allow",
        "Action": "ssm:SendCommand",
        "Resource": [
            f"arn:aws:ec2:{AWS_REGION}:{AWS_ACCOUNT_ID}:instance/{TC_APP_EC2_INSTANCE_ID}",
            f"arn:aws:ssm:{AWS_REGION}:{AWS_ACCOUNT_ID}:document/Deploy",
        ],
    },
    "ssm:shell:start": {
        "Effect": "Allow",
        "Action": "ssm:StartSession",
        "Resource": [
            f"arn:aws:ec2:{AWS_REGION}:{AWS_ACCOUNT_ID}:instance/{TC_APP_EC2_INSTANCE_ID}",
            f"arn:aws:ssm:{AWS_REGION}:{AWS_ACCOUNT_ID}:document/SSM-SessionManagerRunShell",
        ],
    },
    "ssm:shell:stop": {
        "Effect": "Allow",
        "Action": ["ssm:TerminateSession", "ssm:ResumeSession"],
        "Resource": "arn:aws:ssm:*:*:session/${aws:username}-*",
    },
    "ssm:shell:status": {
        "Effect": "Allow",
        "Action": [
            "ssm:DescribeSessions",
            "ssm:GetConnectionStatus",
            "ssm:DescribeInstanceInformation",
            "ec2:DescribeInstances",
        ],
        "Resource": "*",
    },
    "AWS_Lambda_FullAccess": "arn:aws:iam::aws:policy/AWSLambda_FullAccess",
    "AmazonSSMManagedInstanceCore": "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
    "AmazonS3FullAccess": "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    "AWSLambdaVPCAccessExecutionRole": "arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole",
}


trust_policies = {
    "lambda": {
        "Effect": "Allow",
        "Principal": {"Service": "lambda.amazonaws.com"},
        "Action": "sts:AssumeRole",
    },
    "ec2": {
        "Effect": "Allow",
        "Principal": {"Service": "ec2.amazonaws.com"},
        "Action": "sts:AssumeRole",
    },
    "github": {
        "Effect": "Allow",
        "Principal": {
            "Federated": f"arn:aws:iam::{AWS_ACCOUNT_ID}:oidc-provider/token.actions.githubusercontent.com"
        },
        "Action": "sts:AssumeRoleWithWebIdentity",
    },
    "user": {
        "Effect": "Allow",
        "Principal": {"AWS": f"arn:aws:iam::{AWS_ACCOUNT_ID}:root"},
        "Action": "sts:AssumeRole",
    },
}

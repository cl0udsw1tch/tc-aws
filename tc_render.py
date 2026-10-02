from config import AWS_ACCOUNT_ID, AWS_REGION
from policies import permission_policies, trust_policies

tc_render_role_trust_policy = [trust_policies["lambda"]]

tc_render_role_identity_policies = [
    permission_policies["AmazonS3FullAccess"],
    permission_policies["AWSLambdaVPCAccessExecutionRole"],
]

tc_render = {
    "name": "tc-render",
    "trust": tc_render_role_trust_policy,
    "identity": tc_render_role_identity_policies,
}

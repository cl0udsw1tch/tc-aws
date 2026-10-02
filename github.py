from config import AWS_ACCOUNT_ID, AWS_REGION, TC_APP_EC2_INSTANCE_ID
from policies import permission_policies, trust_policies

github_trust_policy = [trust_policies["github"]]
github_identity_policies = [
    permission_policies["ssm:cmd:exec"],
    permission_policies["ssm:cmd:read"],
]

github = {
    "name": "github",
    "trust": github_trust_policy,
    "identity": github_identity_policies,
}

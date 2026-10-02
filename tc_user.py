from config import AWS_ACCOUNT_ID, AWS_REGION, TC_APP_EC2_INSTANCE_ID
from policies import permission_policies, trust_policies

# Role: TcDeploy (run the deploy document only)
tc_dev_trust_policy = [trust_policies["user"]]
tc_dev_permission_policies = [
    permission_policies["ssm:cmd:deploy"],
    permission_policies["ssm:cmd:read"],
    permission_policies["ssm:shell:start"],
    permission_policies["ssm:shell:status"],
    permission_policies["ssm:shell:stop"],
]

tc_dev = {
    "name": "user/tc-dev",
    "trust": tc_dev_trust_policy,
    "identity": tc_dev_permission_policies,
}

tc_read = {
    "name": "user/tc-read",
    "trust": tc_dev_trust_policy,
    "identity": [permission_policies["ssm:cmd:read"]],
}

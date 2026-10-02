from config import VERSION
from policies import permission_policies, trust_policies

tc_app_role_trust_policy = [
    trust_policies["ec2"],
]

tc_app_role_identity_policies = [
    permission_policies["AWS_Lambda_FullAccess"],
    permission_policies["AmazonSSMManagedInstanceCore"],
]

tc_app = {
    "name": "tc-app",
    "trust": tc_app_role_trust_policy,
    "identity": tc_app_role_identity_policies,
}

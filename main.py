import json
import os
from os import path

from config import VERSION
from github import github
from tc_app import tc_app
from tc_render import tc_render
from tc_user import tc_dev, tc_read

roles = [tc_dev, github, tc_app, tc_render, tc_read]

POLICIES_DIR = os.path.join(os.getcwd(), "policies")
if not os.path.exists(POLICIES_DIR):
    os.makedirs(POLICIES_DIR)


def create_role_policies(role):
    trust_policy = role["trust"]
    TRUST_POLICY_PATH = os.path.join(POLICIES_DIR, f"{role['name']}/trust.json")
    if not os.path.exists(TRUST_POLICY_PATH):
        os.makedirs(path.dirname(TRUST_POLICY_PATH), exist_ok=True)

    with open(TRUST_POLICY_PATH, "w") as f:
        json.dump(trust_policy, f, indent=2)

    IDENTITY_POLICY_PATH = os.path.join(POLICIES_DIR, f"{role['name']}/identity.json")
    if not os.path.exists(IDENTITY_POLICY_PATH):
        os.makedirs(path.dirname(IDENTITY_POLICY_PATH), exist_ok=True)

    identity_policies = role["identity"]
    with open(IDENTITY_POLICY_PATH, "w") as f:
        json.dump(identity_policies, f, indent=2)


if __name__ == "__main__":
    [create_role_policies(role) for role in roles]

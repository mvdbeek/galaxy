"""
Run this script from galaxy's root with
```
python scripts/populate_vault_secret.py -c config/galaxy.yml -u <user_email> -k <vault_location> -v <value_secret_value>
```
"""

import argparse
import logging
import os
import sys


sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "lib")))

# Set global log level to ERROR
logging.basicConfig(level=logging.ERROR)

WARNING_MODULES = ["parso", "asyncio", "galaxy.datatypes"]
for mod in WARNING_MODULES:
    logger = logging.getLogger(mod)
    logger.setLevel("ERROR")

HELP = """
============
Populate vault secrets for a user
"""


def write_secret(app, user_email: str, secret_key: str, secret_value: str):
    """Write a vault secret for a user."""
    from galaxy.model import User
    from galaxy.security.vault import UserVaultWrapper

    user = app.model.context.query(User).where(User.email == user_email).first()
    if not user:
        print(f"User with email {user_email} not found.")
        return
    user_vault = UserVaultWrapper(app.vault, user)
    user_vault.write_secret(secret_key, secret_value)
    print(f"Vault secret for user {user_email} set")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate vault secrets for a user")
    parser.add_argument("-c", "--config", help="Path to Galaxy configuration file")
    parser.add_argument("-u", "--user-email", required=True, help="Email address of the user")
    parser.add_argument("-k", "--secret-key", required=True, help="Key name for the vault secret")
    parser.add_argument("-v", "--secret-value", required=True, help="Value to store in the vault")

    args = parser.parse_args()

    if args.config:
        os.environ["GALAXY_CONFIG_FILE"] = args.config
    assert os.environ.get(
        "GALAXY_CONFIG_FILE"
    ), "GALAXY_CONFIG_FILE environment variable not set and no config file provided"

    # Import after setting GALAXY_CONFIG_FILE to ensure it's picked up
    from galaxy.celery import get_galaxy_app

    app = get_galaxy_app()
    assert app, "Failed to initialize Galaxy application"
    write_secret(app, args.user_email, args.secret_key, args.secret_value)

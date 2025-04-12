import os

secret_user = os.environ.get("secret_user", "DefaultUser")
print(f"Hello, {secret_user}")
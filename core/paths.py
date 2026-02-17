import os

# HARD ROOT (do not derive from __file__)
PROJECT_ROOT = r"C:\umberlla_corp"

WORKSPACE_ROOT = os.path.join(PROJECT_ROOT, "atlas_workspace")
CODE_DIR = os.path.join(WORKSPACE_ROOT, "code")

os.makedirs(CODE_DIR, exist_ok=True)

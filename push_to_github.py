import os
import subprocess
import sys


PROJECT_DIR = r"c:\Users\Administrator\ALEXX"
REMOTE_URL = "https://github.com/alexanderassi789-tech/AlexBankProject.git"


def run(cmd, check=True):
    print("$", " ".join(cmd))
    result = subprocess.run(cmd, cwd=PROJECT_DIR, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if check and result.returncode != 0:
        raise SystemExit(result.returncode)
    return result


def main():
    run(["C:\\Program Files\\Git\\bin\\git.exe", "status", "--short", "--branch"])
    run(["C:\\Program Files\\Git\\bin\\git.exe", "add", "."])
    commit_message = input("Enter a commit message: ").strip() or "Update project"
    run(["C:\\Program Files\\Git\\bin\\git.exe", "commit", "-m", commit_message])
    run(["C:\\Program Files\\Git\\bin\\git.exe", "remote", "add", "origin", REMOTE_URL], check=False)
    run(["C:\\Program Files\\Git\\bin\\git.exe", "push", "-u", "origin", "main"])
    print("\nDone. Your changes were pushed to GitHub.")


if __name__ == "__main__":
    main()

import os
import subprocess
import sys

def create_virtual_environment(env_name="aws_study_env"):
    """Create a virtual environment."""
    print(f"Creating virtual environment '{env_name}'...")
    subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
    print(f"Virtual environment '{env_name}' created successfully.")

def install_packages(env_name="aws_study_env"):
    """Install necessary packages in the virtual environment."""
    print(f"Installing packages in the virtual environment '{env_name}'...")
    packages = [
        "boto3",        # AWS SDK for Python
        "requests",     # HTTP library
        "pytest",       # Testing framework
        "ipython",      # Interactive Python shell
    ]
    subprocess.run([os.path.join(env_name, "bin", "pip"), "install"] + packages, check=True)
    print(f"Packages installed successfully.")

def main():
    env_name = "aws_study_env"
    create_virtual_environment(env_name)
    install_packages(env_name)
    print("Setup complete. To activate the virtual environment, run:")
    print(f"source {env_name}/bin/activate")

if __name__ == "__main__":
    main()

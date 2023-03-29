import sys
import subprocess

def find_python3_command():
    major, minor = sys.version_info[:2]
    if major == 3:
        return sys.executable
    else:
        try:
            # Check if 'python3' command is available
            subprocess.run(["python3", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return "python3"
        except subprocess.CalledProcessError:
            pass
        except FileNotFoundError:
            pass

        # Check if 'python' command is actually Python 3
        try:
            output = subprocess.run(["python", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            version = output.stderr.decode('utf-8').strip().split()[1]
            major, minor = map(int, version.split('.')[:2])
            if major == 3:
                return "python"
        except subprocess.CalledProcessError:
            pass
        except FileNotFoundError:
            pass

    return None

python3_command = find_python3_command()

if python3_command:
    print(f"'{python3_command}'")
else:
    print("null")

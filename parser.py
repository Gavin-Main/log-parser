import re
from collections import defaultdict


# Path to the log file
LOG_FILE_PATH = 'sample_logs/auth.log'


# Regular expression to match failed SSH login lines and extract IPs
FAILED_LOGIN_REGEX = r'Failed password.*from\s(\d+\.\d+\.\d+\.\d+)'


def parse_ssh_log(file_path):
    """
    Parses an SSH log file to find failed login attempts and return IP counts.


    Arguments:
        file_path (str): Path to the log file.


    Returns:
        dict: Dictionary with IP addresses as keys and failure counts as values.
    """
    ip_counts = defaultdict(int)


    try:
        with open(file_path, 'r') as log_file:
            for line in log_file:
                match = re.search(FAILED_LOGIN_REGEX, line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] += 1


    except FileNotFoundError:
        print(f"[!] Log file not found: {file_path}")
    except Exception as e:
        print(f"[!] An error occurred: {str(e)}")


    return ip_counts


def print_report(ip_counts):
    """
    Prints a summary report of failed login attempts by IP address.


    Arguments:
        ip_counts (dict): Dictionary of IPs and their failure counts.
    """
    print("\n[!] Failed SSH Login Attempts by IP:\n")
    if not ip_counts:
        print("No failed login attempts found.")
    else:
        for ip, count in ip_counts.items():
            print(f" - {ip} -> {count} time(s)")


if __name__ == "__main__":
    ip_failures = parse_ssh_log(LOG_FILE_PATH)
    print_report(ip_failures)

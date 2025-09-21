# log-parser
Overview
  This project is a basic SSH log parser built in Python, designed to detect and report failed login attempts from system log files (e.g., /var/log/auth.log). It solves the problem of manually sifting through large volumes of logs by automatically extracting and counting failed SSH login attempts per IP address. This is highly relevant in cybersecurity as it helps identify brute-force attacks or unauthorized access attempts. The tool provides a quick snapshot of potentially malicious activity, making it valuable for SOC analysts, incident responders, and learners who are developing foundational skills in log analysis, threat detection, and Python scripting.

Features
  - Parses SSH log files to detect failed login attempts
  - Uses regular expressions to accurately extract IP addresses from
    failed log entries
  - Counts and groups failed attempts by IP address
  - Handles missing or unreadable log files with error messages
  - Prints a clean, readable summary report of suspicious IPs and how
    many times they failed to log in
  - Beginner-friendly Python code that is easy to understand and modify
  - Useful for basic intrusion detection or log analysis practice
    
Tools & Technologies
  - Python 3 - Main programming language used for scripting and log parsing
  - Regular Expressions (re module) - for pattern matching and extracting IP addresses from logs
  - Collections.defaultdict - To simplify counting failed login attempts
  - Linux log files (auth.log) - Sample data source simulating real-world  system logs
  - VS Code - Code editor used during development
  - Command Line (CLI) - For running and testing the script

Setup & Installation
# In your CLI, clone the repository
git clone
https://github.com/gavin-main/log-parser

# Navigate into the project
cd log-parser

# Check that you have the latest version of Python installed
Python3 --version

# Run the script
	Python3 parser.py

# These instructions will use the auth.log file provided in the sample_logs directory, but you can also create your own sample log file and place it in the sample_logs directory to be used by the log parser.

Usage Examples
![Running program in CLI Step-by-Step](images\CLI-instructions.png)
Description: Using Windows CLI to clone Git Repository, navigate to the project directory, check for Python3, and run the log parser script.

![Contents of Sample Log being parsed](images\auth.log-contents/png)
Description: This screenshot displays the contents of the sample log I created in order to be parsed by my script.

![Parser Script](images\parser-script)
Description: This screenshot shows the contents of the python script used to parse log files.

Project Structure
log-parser\
|---sample_logs\                 # Directory containing sample log file
|---|---auth.log                 # Sample log file with failed SSH login attempts
|---images\                      # Directory containing screenshots
|---|---auth.log-contents.png    # Contents of sample log
|---|---CLI-instructions.png     # Command Line Steps
|---|---parser-script.png        # Python file contents
|---parser.py                    # Log Parser Script
|---README.md                    # Project description

Security Context / Learning Outcomes
  This project highlights important cybersecurity concepts like log monitoring and intrusion detection by analyzing SSH logs for failed login attempts. It demonstrates how identifying suspicious IP addresses through log parsing can reveal potential brute-force attacks or unauthorized access attempts. While simple, this script reflects the basic process behind real-world security tools like SIEMs that collect and analyze logs to detect threats. Working on this project helped me build practical skills in analyzing security logs and understanding how defenders use data to spot indicators of compromise, which is essential for roles in SOC analysis and threat hunting.

Future Improvements
 1. Add geo-IP lookup to show where the attackers are coming from
 2. Save results to a CSV or JSON file for analysis
 3. Whitelist internal IPs or known addresses
 4. Sort output by number of attempts, highest first
 5. Add support for other log formats, like FTP or web server logs

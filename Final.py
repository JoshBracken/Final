#!/usr/bin/env python3
"""
Josh Bracken
Final Project
5/10/23
"""
# This code uses the Python requests module to make HTTP requests to the Cisco DNA Center API
# in order to retrieve device health information.
# The API URL and authentication credentials are defined at the beginning of the script.
# A try/except block is used to catch any exceptions that may be raised while executing the code within the block.
# Within the block, the script makes a POST request to the API URL using the authentication credentials,
# and disables SSL verification. The API response is then parsed as JSON, and the authentication token is extracted
# from the response and stored in the headers.
# Next, the script makes a GET request to the API URL, this time including the authentication token in the headers.
# The response is parsed as JSON, and device health information is extracted from the response and stored in a list.
# Finally, the script uses a string method to format and print the device health information in a tabular format.
# If any exceptions occur during execution, they are caught and printed to the console.

import requests

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
username = "devnetuser"
password = "Cisco123!"
headers = {"Content-Type": "application/json"}

# try/except block to catch any exceptions that may be raised while executing the code within the block
try:
    # Disable SSL verification
    response = requests.post(url, auth=(username, password), headers=headers, verify=False).json()

    # Access the API utilizing json Dictionary response
    api_url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/device-health"
    headers["X-Auth-Token"] = response["Token"]
    response = requests.get(api_url, headers=headers, verify=False).json()

    # Create a List to store the data device name, CPU Utilization, CPU Health and Memory Utilization
    device_data = []

    for device in response["response"]:
        name = device["name"]
        cpu_utilization = device.get("cpuUtilization", "N/A")
        cpu_health = device.get("cpuHealth", "N/A")
        mem_utilization = device.get("memoryUtilization", "N/A")
        device_data.append([name, cpu_utilization, cpu_health, mem_utilization])

    # Print the output in a formatted way using a String method to make a columned output that I spent way too much time
    # playing around with this. Submitting what I have. Have a great summer!
    print("{:<30} {:<20} {:<20} {:<20}".format("name", "CPU Utilization", "CPU Health", "Memory Utilization"))
    print("-" * 90)
    for device in device_data:
        print("{:<30} {:<20} {:<20} {:<20}".format(*device))

except Exception as e:
    print("Error:", e)








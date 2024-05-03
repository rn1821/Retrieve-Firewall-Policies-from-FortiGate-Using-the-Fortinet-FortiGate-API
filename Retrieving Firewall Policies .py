#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import json

# Define the IP address of the FortiGate device
fortigate_ip = 'your_fortigate_ip'

# Define the API key for authentication
api_key = 'your_api_key'

# Construct the URL for the FortiGate API endpoint to retrieve firewall policies
url = f'https://{fortigate_ip}/api/v2/cmdb/firewall/policy'

# Set up HTTP headers including the API key for authentication
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Send a GET request to retrieve firewall policies from the FortiGate API
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    policies_data = response.json()

    # Extract the list of firewall policies from the response data
    firewall_policies = policies_data['results']

    # Iterate over each firewall policy and print relevant information
    for policy in firewall_policies:
        policy_id = policy['policyid']
        source_interface = policy['srcintf']
        destination_interface = policy['dstintf']
        action = policy['action']

        # Print information about the firewall policy
        print(f"Policy ID: {policy_id}")
        print(f"Source Interface: {source_interface}")
        print(f"Destination Interface: {destination_interface}")
        print(f"Action: {action}")
        print()

else:
    # If the request was not successful, print an error message
    print(f"Failed to retrieve firewall policies. Status code: {response.status_code}")


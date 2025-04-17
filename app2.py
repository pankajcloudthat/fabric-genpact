import time
import os
import json
import datetime
import requests

apim_resource_gateway_url = "https://apim33x.azure-api.net"
apim_subscription_key = "0c0a8c90eaaf42e0bfdf39555e910ba3"

openai_api_version = "2025-01-01-preview"
openai_model_name = "gpt-4o-mini"
openai_deployment_name = "gpt-4o-mini-33x"


# Test the API using a direct HTTP call

url = apim_resource_gateway_url + "/openai/deployments/" + openai_deployment_name + "/chat/completions?api-version=" + openai_api_version
# print(url)

payload = {    
    "messages": [
        { "role": "system", "content": "You are a friendly assistant." },
        { "role": "user", "content": "What's a good action hindi movie to watch tonight?" }
    ]
}

headers = {
    'Content-Type': "application/json",
    'api-key':apim_subscription_key
}

response = requests.post(url, headers = headers, json = payload)

# Check the response status code and apply formatting
if 200 <= response.status_code < 300:
    status_code_str = '\x1b[1;32m' + str(response.status_code) + " - " + response.reason + '\x1b[0m'  # Bold and green
elif response.status_code >= 400:
    status_code_str = '\x1b[1;31m' + str(response.status_code) + " - " + response.reason + '\x1b[0m'  # Bold and red
else:
    status_code_str = str(response.status_code)  # No formatting
    
# Print the response status with the appropriate formatting
print("Response status:", status_code_str)

if (response.status_code == 200):
    data = json.loads(response.text)
    print("Token usage:", data.get("usage"), "\n")
    print("💬 ", data.get("choices")[0].get("message").get("content"), "\n")
else:
    print(response.text) 
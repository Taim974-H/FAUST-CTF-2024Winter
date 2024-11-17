import requests
import time
import re

# Start the timer
start_time = time.time()

# URL for the GET and POST requests (replace with actual URLs if needed)
get_url = "https://workshop.faust.ninja:8010/python/level04/"  # Replace with the GET request URL
post_url = "https://workshop.faust.ninja:8010/python/level04/"  # Replace with the POST request URL

# Create a session to reuse the connection
session = requests.Session()

try:
    # Step 1: GET request to retrieve the secret and expression
    get_response = session.get(get_url)
    print(get_response)
    get_response_text = get_response.text

    # Print the GET response for debugging
    print("GET Response Status Code:", get_response.status_code)
    print("GET Response Text:", get_response_text)

    # Step 2: Extract the secret and arithmetic expression using regex
    secret_match = re.search(r"secret is: (.+)", get_response_text)
    expression_match = re.search(r"solve for us: (\d+ \* \d+)", get_response_text)

    if not secret_match or not expression_match:
        print("Failed to extract secret or expression.")
        exit()

    secret = secret_match.group(1).strip()
    expression = expression_match.group(1).strip()

    # Calculate the result of the expression
    result = eval(expression)

    # Step 3: POST request with the extracted secret and calculated result
    payload = {
        "secret": secret,
        "result": result
    }

    # Send the POST request
    post_response = session.post(post_url, data=payload)

    # Print the POST response for debugging
    print("POST Response Status Code:", post_response.status_code)
    print("POST Response Text:", post_response.text)

except Exception as e:
    print("An error occurred:", str(e))

# End the timer and check the elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")
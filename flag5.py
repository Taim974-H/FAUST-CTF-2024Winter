import requests
import time
import re

get_url = "https://workshop.faust.ninja:8010/python/level05/"
post_url = "https://workshop.faust.ninja:8010/python/level05/"

# Start the timer to ensure we complete within 1 second
start_time = time.time()
session = requests.Session()

try:
    # First GET request to retrieve the first 50 values
    first_response = session.get(get_url)
    first_values = first_response.text

    # Extract the content within <tt> tags using regex
    f_tt_content = re.search(r"<tt>(.*?)</tt>", first_values, re.DOTALL)
    f_values = re.split(r"<br\s*/?>", f_tt_content.group(1))
    f_extracted_values = [value.strip() for value in f_values if value.strip()]
    
    print("First values:", f_extracted_values)

    # =================================================================

    # Second GET request to retrieve the 51 values (including the new one)
    second_response = session.get(get_url)
    second_values = second_response.text

    # Extract the content within <tt> tags for the second response
    tt_content_second = re.search(r"<tt>(.*?)</tt>", second_values, re.DOTALL)
    second_values_list = re.split(r"<br\s*/?>", tt_content_second.group(1))
    second_extracted_values = [value.strip() for value in second_values_list if value.strip()]
    
    print("Second values:", second_extracted_values)

    # Step 3: Find the new value by finding the difference between the two sets
    first_set = set(f_extracted_values)
    second_set = set(second_extracted_values)

    new_value_set = second_set - first_set

    if len(new_value_set) != 1:
        print("Error: More than one new value detected or no new value found.")
        exit()

    new_value = new_value_set.pop()
    
    print("New value:", new_value)

    # Step 4: Send the new value via POST request
    payload = {"new_value": new_value}
    post_response = session.post(post_url, data=payload)

    # Print POST response (for debugging)
    print("POST Response Status Code:", post_response.status_code)
    print("POST Response Text:", post_response.text)

except Exception as e:
    print("An error occurred:", str(e))

# End the timer and check elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.4f} seconds")

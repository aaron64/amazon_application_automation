import json
import webbrowser
import requests

# set black-list terms for title and qualifications sections
qualifications_blacklist = ["industry experience", "professional software", "professional experience", "years in enterprise", "masters degree", "Ph.D degree"]
title_blacklist = ["Sr.", "Senior", "Manager"]

response = requests.get("https://www.amazon.jobs/en/search.json?base_query=&city=Seattle&country=USA&county=King&facets%5B%5D=location&facets%5B%5D=business_category&facets%5B%5D=category&facets%5B%5D=schedule_type_id&facets%5B%5D=employee_class&facets%5B%5D=normalized_location&facets%5B%5D=job_function_id&latitude=47.60358&loc_group_id=&loc_query=Seattle%2C+WA%2C+United+States&longitude=-122.32945&offset=0&query_options=&radius=24km&region=Washington&result_limit=100&schedule_type_id%5B%5D=Full-Time&sort=relevant")

json_data = response.json()
json_jobs = json_data["jobs"]

for json_job in json_jobs:
    # check posting against blacklist
    valid = True
    for qualification in qualifications_blacklist:
        if qualification in json_job["basic_qualifications"]:
            valid = False
            break

    for title in title_blacklist:
        if title in json_job["title"]:
            valid = False
            break

    if valid:
        print("\n\n\n\n\n")

        print(json_job["title"])
        print("____________________________________\n")

        print("Description:")
        print(json_job["description"])
        print()

        print("Qualifications:")
        print(json_job["basic_qualifications"])
        print()

        # get input
        apply_input = ""
        while apply_input is not "y" and apply_input is not "n":
            apply_input = input("Apply? (y/n)")
            print(apply_input)
        if apply_input is "y":
            webbrowser.open(json_job["url_next_step"])
        

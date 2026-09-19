from jobs import get_all_jobs


jobs = get_all_jobs()

print("----- AVAILABLE JOBS -----")

for job in jobs:
    print(
        job["title"],
        "|",
        job["company"],
        "|",
        job["location"]
    )

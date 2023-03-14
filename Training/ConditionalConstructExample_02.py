#job_title is engineer then commission .05
# job_title is doctor then commision .06
# job_title is lawyer then commision .75
# for others - commision .02
job_title='clerk'
sal=50000
if job_title=='engineer':
    comm=sal*.05
    print(f"Job  {job_title}\nSalary is {sal}\nCommision is {comm}")
elif job_title=='doctor':
    comm = sal * .06
    print(f"Job  {job_title}\nSalary is {sal}\nCommision is {comm}")
elif job_title=='lawyer':
    comm = sal * .075
    print(f"Job  {job_title}\nSalary is {sal}\nCommision is {comm}")
else:
    comm = sal * .02
    print(f"Job  {job_title}\nSalary is {sal}\nCommision is {comm}")
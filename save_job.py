import pandas as pd

def save_file(jobs):
    save = pd.DataFrame(jobs)
    save = save[['기업','주 업무','위치','경력']]
    save.head()
    save.to_csv("/home/geonoo/바탕화면/myProject/developer_jobs/developer_jobs_save.csv")

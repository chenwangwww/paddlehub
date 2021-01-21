from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

def job():
    print(datetime.now().strftime(r"%Y-%m-%d %H:%M:%S"))
def job2():
    print('job2')
sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=2)
sched.add_job(job2, 'interval', seconds=4)
sched.start()
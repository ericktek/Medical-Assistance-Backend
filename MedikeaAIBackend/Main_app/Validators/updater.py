from apscheduler.schedulers.background import BackgroundScheduler
from .trainMl import startTraining

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(startTraining, 'interval', minutes=60)
    scheduler.start()
    

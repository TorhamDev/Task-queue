from redis import Redis
from time import sleep

redis_db = Redis("localhost", 6379, 0)
DEFAULT_QUEUE = "default"

while True:
    task = redis_db.rpop(DEFAULT_QUEUE)
    if task != None:
        print(f"Doing Task {task.decode()} ...")
        sleep(10)

import queue
import threading
import time

# Define a function to perform a task
def perform_task(task_id):
    print(f"Starting task {task_id}")
    # Do some work here
    time.sleep(0.25)
    print(f"Finished task {task_id}")

# Define a worker function to process tasks
def worker(task_queue):
    while True:
        task = task_queue.get()
        #task_queue.join()
        #task2 = task_queue.get()
        #print(task2)
        if task is None:
            break
        perform_task(task)
        task_queue.task_done()

# Create a queue and some worker threads
task_queue = queue.Queue()
worker_threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(task_queue,))
    t.start()
    worker_threads.append(t)

# Add some tasks to the queue
for i in range(5):
    task_queue.put(i)

print(task_queue)

# Wait for all tasks to be completed
task_queue.join()

# Signal the worker threads to exit
for t in worker_threads:
    task_queue.put(None)
for t in worker_threads:
    t.join()



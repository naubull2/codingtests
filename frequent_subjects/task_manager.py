# coding: utf-8
"""
Simple multithread task manager
__author_ = 'naubull2 (naubull2@gmail.com)'
"""
import logging
import random
import json
import time
import atexit
from queue import Queue
from threading import Thread

logger = logging.getLogger("dialog-tool")


class Worker(Thread):
    """
    Thread executing tasks from a given tasks queue
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        # run as daemon thread in background
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, kwargs = self.tasks.get()
            try:
                func(**kwargs)

            except Exception as e:  # pylint: disable=broad-except
                logger.error(f"Evaluator Error: {str(e)}")

            finally:
                # Mark this task as done, whether an exception happened or not
                self.tasks.task_done()


class ThreadPool(object):
    """
    Pool of threads consuming tasks from a queue
    - add_task()
      : Worker thread runs func(**kwargs)
      : busy waiting for a task
    - graceful_stop()
      : Wait until all running jobs are done
    """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, handler, **kwargs):
        """
        Add a task to the queue
        """
        self.tasks.put((handler, kwargs))

    def graceful_stop(self):
        """
        Wait for completion of all the tasks in the queue
        """
        self.tasks.join()


class EvaluationTaskManager(object):
    """
    Class for centralized managing of new evaluation tasks
    """

    def __init__(self, pool_size=5):
        self.pool = ThreadPool(pool_size)
        atexit.register(self.finalize)

    def add_task(self, handler, **kwargs):
        """
        Runs handler function with **kwargs
        """
        self.pool.add_task(handler, **kwargs)

    def finalize(self):
        """
        Registered as 'atexit' handler
        """
        logger.info("MANAGER: Waiting for all jobs to finish")
        self.pool.graceful_stop()  # wait until all evaluations are finished
        logger.info("MANAGER: all jobs are finished")


if __name__ == "__main__":
    import requests

    ###############################################################################
    # NOTE Last task is finished the last, check that threads are gracefully joined
    #
    # Success in handler api1: Sup.
    # Success in handler api2: Sleep tight.
    # MANAGER: Waiting for all jobs to finish
    # Success in handler api3: Yeah lets meet after lunch
    # MANAGER: all jobs are finished
    ###############################################################################

    task_manager = EvaluationTaskManager(pool_size=2)

    def sample_handler(name, url, q):
        """make a delayed call to the given API url, print output response to the logger"""
        time.sleep(random.random() * 10)
        try:
            ret = requests.get(url, params={"q": q}).json()
        except Exception as e:
            logger.error(f"Error in handler {name}: {str(e)}")
        else:
            logger.info(f'Success in handler {name}: {ret["output"]}')

    # Supoose localhost is running a conversation API on port 8988
    task_manager.add_task(
        sample_handler,
        name="api1",
        url="http://localhost:8988/chat",
        q="Hey what's up"
    )
    task_manager.add_task(
        sample_handler,
        name="api2",
        url="http://localhost:8988/chat",
        q="Good night"
    )
    task_manager.add_task(
        sample_handler,
        name="api3",
        url="http://localhost:8988/chat",
        q="We had a lunch meeting tommorow?",
    )
    time.sleep(10)

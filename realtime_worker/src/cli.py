import json
import multiprocessing
from multiprocessing import Process
from typing import Optional
import time
import uuid
from pathlib import Path


class WorkerPoolManager:
    """
    swam worker context and worker management
    """

    n_workers: int
    worker_id: uuid
    procs: list

    def __init__(self):

        # number of workers
        self.n_workers = 0

        # worker id with uuid
        self.worker_id = uuid.uuid4()

        # number of process
        self.procs = []

    def worker_pool_exec(self):
        """
        pool worker
        """
        pass


class WorkerPoolExecutor:
    """
    call worker pool manager and pooling worker
    """

    wpm: Optional[WorkerPoolManager]
    prev_worker_info: dict
    new_worker_info: dict
    f_path: str

    def __init__(self):
        self.wpm = WorkerPoolManager()
        self.prev_info = {}
        self.new_worker_info = {}
        self.f_path = "./worker_info.json"

    def json_parser(self):
        """
        parse to worker info json file
        """
        with open(self.f_path, "r") as f:
            json_data = json.load(f)

        print(json_data)

    def start(self):
        """
        worker pool executor starter
        """
        self.json_parser()
        p = Process()


if __name__ == "__main__":
    wpe: Optional[WorkerPoolExecutor] = WorkerPoolExecutor()
    wpe.start()

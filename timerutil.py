import time
import logger


class TimerUtil:
    def __init__(self):
        self.start_time = time.time()

    def stop_timer(self):
        time_taken = time.time() - self.start_time
        logger.info("Time taken = {0}".format(time_taken))
        return time_taken

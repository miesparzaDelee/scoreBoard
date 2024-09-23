import threading
import time

class StopwatchTimer:
    def __init__(self, time_mins, direction="up"):
        """
        Initialize the threaded stopwatch timer.
        
        :param time_mins: The time in minutes to count up or down.
        :param direction: 'up' for counting up, 'down' for counting down.
        """
        self.time_mins = time_mins * 60  # Convert minutes to seconds
        self.direction = direction
        self.current_time = 0 if direction == "up" else self.time_mins
        self.running = False
        self.time_finished = False
        self.subscribers = []  # List of tuples: (callback, trigger_interval)
        self.finalized_subscribers = []  # List to hold callbacks for when time finishes
        self.lock = threading.Lock()  # To manage shared access to current_time
        self.last_trigger_times = {}  # Store the last trigger times for each callback
        self.start_time = None  # Track the time the timer started

    def subscribe_on_elapsed(self, callback, trigger_interval):
        """
        Subscribe a callback that triggers every `trigger_interval` seconds.
        
        :param callback: The function to call.
        :param trigger_interval: The time in seconds after which to call the callback.
        """
        self.subscribers.append((callback, trigger_interval))
        
        # Initialize last_trigger_times based on whether the timer is counting up or down
        if self.direction == "up":
            self.last_trigger_times[callback] = 0  # Start from 0 when counting up
        else:
            self.last_trigger_times[callback] = self.time_mins  # Start from time_mins when counting down


    def subscribe_on_finish(self, callback):
        """Subscribe to the event that triggers when the timer finishes."""
        self.finalized_subscribers.append(callback)

    def notify_finalized_subscribers(self):
        """Notify subscribers when the timer finishes."""
        for callback in self.finalized_subscribers:
            callback()

    def notify_subscribers(self):
        """Notify subscribers based on their elapsed time triggers."""
        with self.lock:
            elapsed_time = self.current_time

        for callback, trigger_interval in self.subscribers:
            # Handle counting up or down by checking time difference based on the direction
            if self.direction == "up":
                while elapsed_time - self.last_trigger_times[callback] >= trigger_interval:
                    callback(self.get_current_time())
                    self.last_trigger_times[callback] += trigger_interval
            else:  # Handle counting down
                while self.last_trigger_times[callback] - elapsed_time >= trigger_interval:
                    callback(self.get_current_time())
                    self.last_trigger_times[callback] -= trigger_interval
   
    def _run_timer(self):
        """Thread that runs the timer and triggers the callback."""
        self.start_time = time.perf_counter()
        while self.running and not self.time_finished:
            with self.lock:
                elapsed = time.perf_counter() - self.start_time
                self._update_time(elapsed)

            self.notify_subscribers()
            time.sleep(0.001)  # Sleep briefly to reduce CPU usage


        if self.time_finished:
            self.notify_finalized_subscribers()

    def _update_time(self, elapsed):
        """Update the timer based on the elapsed time."""
        if self.direction == "up":
            self.current_time = elapsed
            if self.current_time >= self.time_mins:
                self.current_time = self.time_mins
                self.time_finished = True
                self.stop()
        else:
            self.current_time = self.time_mins - elapsed
            if self.current_time <= 0:
                self.current_time = 0
                self.time_finished = True
                self.stop()

    def start(self):
        """Start the timer in a separate thread."""
        if not self.running and not self.time_finished:
            self.running = True
            self.thread = threading.Thread(target=self._run_timer)
            self.thread.start()

    def stop(self):
        """Stop the timer and wait for the thread to finish."""
        if self.running:
            self.running = False
             # We do not call self.thread.join() inside the thread that is running.
        if threading.current_thread() != self.thread:
            self.thread.join()  # Only join if stop is called from outside the running thread

    def reset(self):
        """Reset the timer and allow it to be started again."""
        with self.lock:
            self.current_time = 0 if self.direction == "up" else self.time_mins
            self.time_finished = False
            self.running = False
            self.last_trigger_times = {}

    def get_current_time(self):
        """Return the current time in minutes and seconds (seconds as float)."""
        with self.lock:
            total_seconds = self.current_time
            minutes, seconds = divmod(total_seconds, 60)  # Don't cast to int, so seconds can have decimals
        return int(minutes), seconds  # Minutes as an integer, seconds as a float

# This section will only run if the file is executed directly
if __name__ == "__main__":
    def on_time_finished(init_time):
        final_time = time.perf_counter() - init_time
        print(f"Time is up! {final_time:.3f} elapsed")

    def on_second_elapsed(current_time):
        minutes, seconds = current_time
        print(f"1 Second Callback: Elapsed time: {minutes} minutes, {seconds:.2f} seconds")

    # Create a stopwatch timer (1-minute countdown)
    stopwatch_timer = StopwatchTimer(1, "down")

    # Subscribe the callback with a trigger interval of 1 second
    stopwatch_timer.subscribe_on_elapsed(on_second_elapsed, 1)
    
    # Subscribe to the time-finished event
    stopwatch_timer.subscribe_on_finish(lambda: on_time_finished(init_time))

    # Start the timer
    init_time = time.perf_counter()
    stopwatch_timer.start()

    # Simulate querying the current time every 5 seconds
    while stopwatch_timer.running:
        time.sleep(1)
        # Get the current time (in minutes and seconds)
        minutes, seconds = stopwatch_timer.get_current_time()
        print(f"Queried time: {minutes} minute(s) and {seconds:.2f} second(s)")


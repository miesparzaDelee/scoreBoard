import unittest
import time
from stopwatch_timer import StopwatchTimer

class TestStopwatchTimer(unittest.TestCase):

    def setUp(self):
        """Set up the stopwatch timer before each test."""
        self.stopwatch_timer = StopwatchTimer(1, "down")  # 1-minute countdown
        self.elapsed_events = []
        self.finished_event_triggered = False

    def on_second_elapsed(self, current_time):
        """Callback to collect second elapsed events."""
        minutes, seconds = current_time
        self.elapsed_events.append((minutes, seconds))

    def on_time_finished(self):
        """Callback to collect the finished event."""
        self.finished_event_triggered = True

    def test_initialization(self):
        """Test that the timer is initialized correctly."""
        self.assertEqual(self.stopwatch_timer.time_mins, 60)  # 1 minute = 60 seconds
        self.assertEqual(self.stopwatch_timer.direction, "down")
        self.assertEqual(self.stopwatch_timer.current_time, 60)
        self.assertFalse(self.stopwatch_timer.running)

    def test_start_and_stop_timer(self):
        """Test starting and stopping the timer."""
        self.stopwatch_timer.start()
        self.assertTrue(self.stopwatch_timer.running)

        time.sleep(2)  # Sleep for 2 seconds to simulate time passage
        self.stopwatch_timer.stop()
        self.assertFalse(self.stopwatch_timer.running)

        # Check that time has decreased
        minutes, seconds = self.stopwatch_timer.get_current_time()
        self.assertLess(self.stopwatch_timer.current_time, 60)

    def test_reset_timer(self):
        """Test that the timer can be reset correctly."""
        self.stopwatch_timer.start()
        time.sleep(2)
        self.stopwatch_timer.stop()

        # Reset the timer
        self.stopwatch_timer.reset()
        minutes, seconds = self.stopwatch_timer.get_current_time()
        self.assertEqual(self.stopwatch_timer.current_time, 60)  # Should reset to 1 minute

    def test_subscribe_on_elapsed(self):
        """Test that the second-elapsed event is triggered properly."""
        # Subscribe to the second-elapsed event
        self.stopwatch_timer.subscribe_on_elapsed(self.on_second_elapsed, 1)

        self.stopwatch_timer.start()

        # Simulate waiting for 5 seconds
        time.sleep(5)
        self.stopwatch_timer.stop()

        # Check that we received 5 events for each second elapsed
        self.assertEqual(len(self.elapsed_events), 5)

        # Check the correctness of the elapsed times
        for i, (minutes, seconds) in enumerate(self.elapsed_events):
            self.assertEqual(minutes, 0)
            self.assertEqual(seconds, 59 - i)

    def test_subscribe_on_finish(self):
        """Test that the time-finished event is triggered correctly."""
        # Subscribe to the time-finished event
        self.stopwatch_timer.subscribe_on_finish(self.on_time_finished)

        self.stopwatch_timer.start()

        # Wait for the timer to run out
        time.sleep(65)  # 65 seconds to ensure timer finishes

        self.stopwatch_timer.stop()

        # Check if the finished event was triggered
        self.assertTrue(self.finished_event_triggered)

    def test_prevent_restart_after_finish(self):
        """Test that the timer does not restart once it has finished."""
        self.stopwatch_timer.start()

        # Wait for the timer to finish
        time.sleep(65)
        self.stopwatch_timer.stop()

        # Try starting the timer again (it should not restart)
        self.stopwatch_timer.start()
        self.assertFalse(self.stopwatch_timer.running)  # Timer should not restart

if __name__ == '__main__':
    unittest.main()

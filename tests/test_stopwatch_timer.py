import unittest
import time
from src.model.stopwatch_timer import StopwatchTimer

class TestStopwatchTimer(unittest.TestCase):

    def setUp(self):
        """Set up a sample stopwatch timer for testing before each test case."""
        self.timer = StopwatchTimer(1, "down")  # Create a 1-minute countdown timer

    def test_initialization(self):
        """Test that the timer is initialized correctly."""
        self.assertEqual(self.timer.time_mins, 60)  # 1 minute is converted to 60 seconds
        self.assertEqual(self.timer.direction, "down")
        self.assertEqual(self.timer.current_time, 60)
        self.assertFalse(self.timer.running)
        self.assertFalse(self.timer.time_finished)

    def test_start_stop(self):
        """Test starting and stopping the timer."""
        self.timer.start()
        time.sleep(0.1)  # Let it run briefly
        self.assertTrue(self.timer.running)
        self.timer.stop()
        self.assertFalse(self.timer.running)

    def test_countdown(self):
        """Test the countdown functionality."""
        self.timer.start()
        time.sleep(1.1)  # Let the timer run for a bit over a second
        self.assertTrue(self.timer.running)
        self.assertLess(self.timer.current_time, 60)  # It should have counted down
        self.timer.stop()

    def test_reset(self):
        """Test resetting the timer."""
        self.timer.start()
        time.sleep(0.1)  # Let it run briefly
        self.timer.stop()
        self.timer.reset()
        self.assertEqual(self.timer.current_time, 60)
        self.assertFalse(self.timer.running)
        self.assertFalse(self.timer.time_finished)

    def test_time_finished_event(self):
        """Test that the time finished event triggers correctly."""
        def on_time_finished():
            self.time_finished_called = True
        
        self.timer = StopwatchTimer(1/60, "down")
        self.time_finished_called = False
        self.timer.subscribe_on_finish(on_time_finished)
        self.timer.start()
        time.sleep(1.1)  # Let the timer reach zero
        self.assertTrue(self.time_finished_called)  # The callback should have been triggered
        self.assertFalse(self.timer.running)

    def test_on_elapsed_callback(self):
        """Test the elapsed callback functionality."""
        def on_second_elapsed(current_time):
            self.elapsed_callback_called = True
            self.elapsed_time = current_time

        self.elapsed_callback_called = False
        self.timer.subscribe_on_elapsed(on_second_elapsed, 1)  # 1-second callback
        self.timer.start()
        time.sleep(1.1)  # Wait for the first callback
        self.assertTrue(self.elapsed_callback_called)
        self.assertLessEqual(self.elapsed_time[1], 59)  # Check that seconds have elapsed
        self.timer.stop()

    def test_callback_triggered(self):
        """Test that the callback triggers at the correct intervals."""
        def on_second_elapsed(current_time):
            self.elapsed_times.append(current_time)

        self.elapsed_times = []
        self.timer.subscribe_on_elapsed(on_second_elapsed, 1)  # 1-second interval
        self.timer.start()
        time.sleep(3.1)  # Let it run for 3 seconds
        self.timer.stop()

        self.assertEqual(len(self.elapsed_times), 3)  # Should have 3 callbacks triggered

if __name__ == '__main__':
    unittest.main()

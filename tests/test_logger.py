import unittest
import logging

from app.logger import Logger


class TestLogger(unittest.TestCase):
    def test_settup(self):
        try:
            Logger.setup()

            logging.info("test info log")
            logging.error("test error log")
        except Exception as e:
            self.fail(f"Logger.setup() raised {type(e).__name__} unexpectedly!")


if __name__ == "__main__":
    unittest.main()

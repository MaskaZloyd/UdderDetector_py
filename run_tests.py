import unittest

test_suite = unittest.TestLoader().discover("tests")
unittest.TextTestRunner(verbosity=2).run(test_suite)

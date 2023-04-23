#!/usr/bin/python3
import unittest
from tests.test_models.test_engine.test_file_storage import test_fileStorage

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_fileStorage)
    unittest.TextTestRunner(verbosity=2).run(suite)

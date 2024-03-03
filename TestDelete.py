import unittest
from RecordController import recordController

"""
    Unit test class for the delete function
"""
class TestDelete(unittest.TestCase):
    def setUp(self):
        self.controller = recordController()

    def test_delete_record(self):
        self.controller.load_records()

        initial_record_count = len(self.controller.model.records)
        self.controller.delete_record(0)
        final_record_count = len(self.controller.model.records)

        """
            Assert for the delete function
        """
        self.assertEqual(final_record_count, initial_record_count - 1)


if __name__ == '__main__':
    unittest.main()

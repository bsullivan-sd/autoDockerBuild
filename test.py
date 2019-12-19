import main
import unittest

class pull_request_test():
    def __init__(self):
        self.file1 = file_test("test1/test1.txt")
        self.file2 = file_test("test2/test2.txt")

    def get_files(self):
        return [self.file1, self.file2]


class file_test():
    def __init__(self, filename):
        self.filename = filename


class TestPullRequest(unittest.TestCase):

    def test_pr(self):
        self.assertEqual(main.return_file_paths_that_have_changed_files(pull_request_test()), ['test1/', 'test2/'])


if __name__ == '__main__':
    unittest.main()
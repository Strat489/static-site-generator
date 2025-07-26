import unittest
from gencontent import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        html = "# This is a title\n\nThis is the content."
        title = extract_title(html)
        self.assertEqual(title, "This is a title")
import json
import os
import tempfile
import unittest
from unittest.mock import patch

from reader import read


class TestReader(unittest.TestCase):
    def test_read(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a temporary file with some JSON content
            content = {"foo": "bar"}
            with open(os.path.join(tmpdir, "output.txt"), "w") as f:
                f.write(json.dumps(content))

            # Redirect stdout to a StringIO object to capture the output
            with patch("sys.stdout") as mock_stdout:
                read(os.path.join(tmpdir, "output.txt"))

                # Check that the output matches the expected content
                mock_stdout.assert_called_once_with("bar\n")
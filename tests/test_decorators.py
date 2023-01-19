import time
from io import StringIO
from unittest.mock import patch

from rousquille_tools.decorators import time_def


def test_time_def_decorator_output():
    expected_stdout = "[time_def] Function: func1 Time: 5.0s\n"

    @time_def
    def func1():
        time.sleep(5)

    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        func1()
        assert fake_stdout.getvalue() == expected_stdout

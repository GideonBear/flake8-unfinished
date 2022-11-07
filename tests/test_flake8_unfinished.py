from pathlib import Path

from ezflake.testing import generate_tests


testdir = Path(__file__).parent / 'tests'
test_flake8_unfinished = generate_tests(testdir)

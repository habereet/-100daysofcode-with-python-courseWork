import pytest

from hello_world import hello_name
from my_unittest import test_hello_world_with_unit_test_fail, test_hello_world_with_unit_test_pass

def main():
	test_hello_world_with_unit_test_fail.main()
	test_hello_world_with_unit_test_pass.unittest.main()

if __name__ == '__main__':
	main()
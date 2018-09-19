import pytest

from hello_world import hello_name
from my_pytest import test_hello_world_with_pytest_fail, test_hello_world_with_pytest_pass

def main():
	test_hello_world_with_pytest_fail.test_hello_name()
	test_hello_world_with_pytest_pass.test_hello_name()

if __name__ == '__main__':
	main()
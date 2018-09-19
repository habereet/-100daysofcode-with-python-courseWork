def fizzbuzz(number):
	# This is not pythonic but I wanted to test myself with ternary testing
	# Return number if the number is not divisible by 3 or 5
	# Return Fizz Buzz if it's divisible by 3 and 5
	# Return Fizz if it's divisible by 3
	# Return Buzz if it's divisible by 5
	return number if number % 3 != 0 and number %5 !=0 else 'Fizz Buzz' if number %3 == 0 and number % 5 == 0 else 'Fizz' if number % 3 == 0 else 'Buzz'
from functools import wraps
import inspect


def make_html(tag):
	#print("1")
	def real_decorator(func):
		#print("2")
		def wrapper(*args, **kwargs):
			#print("3")
			print(f'tag - {tag}, args - {args}, kwargs - {kwargs}, func(*args, **kwargs) - {func(*args, **kwargs)}')
			return(f'<{tag}>{func(*args, **kwargs)}</{tag}>')
			#print("4")
		#print("5")
		return wrapper
	#print("6")
	return real_decorator


@make_html("p")
@make_html("strong")
def get_text(text="I code with PyBites"):
	return text


print(get_text())
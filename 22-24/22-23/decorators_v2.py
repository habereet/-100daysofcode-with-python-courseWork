def make_html(tag, text):
	return(f'<{tag}>{text}</{tag}>')


def get_text(text="I code with PyBites"):
	return text


print(make_html("strong", make_html("p", get_text())))
def count_words(file_contents):
        num_words = len(file_contents.split())
        return num_words

def count_chars(file_contents):
	num_chars = {}
	for char in file_contents.lower():
		if char in num_chars:
			num_chars[char] += 1
		else:
			num_chars[char] = 1
	return num_chars

def sort_on(to_be_sorted):
	return to_be_sorted["num"]

def sorted_chars(num_chars):
	to_be_sorted = []
	for key, value in num_chars.items():
		new_dict = {"char": key, "num": value}
		to_be_sorted.append(new_dict)
	to_be_sorted.sort(reverse=True, key=sort_on)
	return to_be_sorted

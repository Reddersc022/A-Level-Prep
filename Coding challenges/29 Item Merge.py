print("*** Item Merge ***")


def unique(list1: list, list2: list):
	return [i for i in list1 if i not in list2] + [i for i in list2 if i not in list1]


def merge(list1: list, list2: list):
	return list(dict.fromkeys(list1 + list2))


def popular(*args):
	lst = []
	for i in args:
		lst += i

	return list(dict.fromkeys(sorted(lst, key=lst.count, reverse=True)))[:3]

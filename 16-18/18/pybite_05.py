NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list(set([f'{name.split()[0].title()} {name.split()[1].title()}' for name in names]))


def dedup_and_title_case_names1(names):
    """Should return a list of names, each name appears only once"""
    return list(set([f'{name.split()[0].title()} {name.split()[1].title()}' for name in names]))


def myKey(e):
    return e.split()[1][0]


def name_len(e):
    return len(e.split()[0])


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(reverse=True, key=myKey)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names.sort(key=name_len)
    return names[0].split()[0]


print(sort_by_surname_desc(NAMES))
#for name in NAMES:
#	print(myKey(name))
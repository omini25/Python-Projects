from googlesearch import search


def test():
    query = input('What do you want to search? ')
    for s in search(query, start=0, pause=2):
        print(s)


test()

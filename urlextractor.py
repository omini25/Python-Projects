from urllib.request import urlopen

# pageToView =
page = urlopen(input('Website you would like to extract urls: '))
partOfPage = input('What part of the page do you want extracted? ')

# sourcecode = page.read()
# page = urlopen(pageToView)

if partOfPage == 'header':
    print(page.headers)
elif partOfPage == 'footer':
    print(page.footer)
# elif partOfPage == 'source':
# print(sourcecode)
else:
    print('Enter a part of the page to print between "header", "Footer", and "Source"')

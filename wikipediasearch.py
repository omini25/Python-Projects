import wikipedia

query = wikipedia.page(input('What would you like to know? '))
print(query.summary)

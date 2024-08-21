import urllib.request

link = f'https://pokeapi.co/api/v2/ability/battle-armor/'
f = urllib.request.urlopen(link)
myfile = f.read()
print(myfile)
print(myfile.find)
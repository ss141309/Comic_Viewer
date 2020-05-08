from retrieve_search import retrieve
from prettytable import PrettyTable
import retrieve_chap
import img_download

k = input('Search')
l = retrieve.title(k)
m = retrieve.desc(k)

x = PrettyTable()
x.field_names = ['S. No.', 'Title']
for search in enumerate(l):
        x.add_row([search[0]+1, search[1]])

print(x)

ask = int(input('Enter serial number'))
chap = l[ask-1]
chap = retrieve_chap.urlify(chap)
publisher = retrieve_chap.retrieve_info.publisher(chap)
writer = retrieve_chap.retrieve_info.author(chap)
artist = retrieve_chap.retrieve_info.artist(chap)
chapters = retrieve_chap.retrieve_info.chap(chap)

y = PrettyTable()
y.field_names = ['Title', 'Publisher', 'Author', 'Artist']
y.add_row([chap, publisher, writer, artist])
print(y)

z = PrettyTable()
z.field_names = ['S. No.', 'Title']
l2 = list(chapters.values())
del l2[0]
l2 = l2[::-1]
for j in enumerate(l2):
    z.add_row([j[0]+1, j[1]])
print(z)

view = int(input('Select serial number'))
l3 = list(chapters.keys())
l3 = l3[::-1]
ok = l3[view-1]

ko = retrieve_chap.retrieve_info.chap_img(ok)

img_download.dwnld_batch(ko,r'C:\Users\Sameer\Desktop\Comic_Viewer\img\star')

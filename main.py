from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.catalog import Catalog
from modules.cd import Cd
import json

book1 = Book(
    'Tittle test',
    'ini Subject Test',
    None, 
    '1345-5433',
    'Raka Mahendra',
    '08978766674'
)

book2 = Book(
    'Tittle test',
    'ini Subject Test',
    None, 
    '1345-5433',
    'Raka Mahendra',
    '08978766674'
)
book3 = Book(
    'Tittle test',
    'ini Subject Test',
    None, 
    '1345-5433',
    'Raka Mahendra',
    '08978766674'
)

magazine1 = Magazine(
    'Media Cnbcc',
    'edisi 14 Juli 2023',
    None,
    'volume 3',
    '-'
)

magazine2 = Magazine(
    'Media Cnbcc',
    'edisi 14 Juli 2023',
    None,
    'volume 1',
    '-'
)
dvd1 = Dvd(
    'test Dvd1',
    ' ini subject test dvd 1',
    None, 
    None,
    None,
    'Comedy'
)    

        

#input search
input_search = 'test'

#collect data per jenis
book = [book1, book2, book3]
magazine = [magazine1, magazine2]
dvd = [dvd1]

#get data from json
f  = open('files/catalog.json')
data_json = json.load(f)
print(data_json)

# create object from data json
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
             title= item['title'],
            subject= item['subject'],
            upc= item['upc'],
            issbn= item['issbn'],
            authors= item['authors'],
            dss_number= item['dds_number']   
        ))
        
        
#collect all data
catalog_all = [book, magazine, dvd]

input_search = 'test'
results = Catalog(catalog_all).search(input_search)
for index, result in enumerate(results):
    print(f'result ke-{index+1} |{result} ')




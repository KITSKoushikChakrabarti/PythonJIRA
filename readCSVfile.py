import csv
import operator

print('Books sorted by date:\n')
with open('books.csv', newline='') as csvfile:
	books = csv.reader(csvfile, delimiter=',')
	sortedBooks = sorted(books, key=operator.itemgetter(1), reverse=True)
	for title, year, author in sortedBooks:
	    print(title, 'by', author, year)
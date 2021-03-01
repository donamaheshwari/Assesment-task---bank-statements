import csv

CATEGORIES = ['pca', 'imps', 'net txn', 'rrn', 'fund transfer', 'cash deposit', 'emi', 'atd', 'upi', 'credit interest capitalised', 'emi', 'refund', 'loan deposit']
def transcation_category(description):
	for categ in CATEGORIES:
		if categ in description.lower():
			return categ
	return "miscellaneous"
csvfile = open('data.csv', "r")
csv_reader = csv.reader(csvfile, delimiter='|')
fields = next(csv_reader)
result_rows = []
for row in csv_reader:
	row.append(transcation_category(row[3]))
	result_rows.append(row)
fields.append("category")
write_file = open("results.csv", "w")
csv_writer = csv.writer(write_file, delimiter="|")

csv_writer.writerow(fields)
for row in result_rows:
	csv_writer.writerow(row)
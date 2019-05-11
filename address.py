# f = open('upravenaprvniverze.csv', 'r')

output_file = open("zip.csv", "w")

with open ("postaObce.csv") as f:
		header = f.readline()
		header_columns = header.split(";")
		zip_position = header_columns.index('psc')

		output_file.write(header)
	
		zip_list = set()

		for line in f:

			column = line.split(";")
			zip_name = column[zip_position]
			item_found = 0
			

			if not zip_name in zip_list:
				zip_list.add(zip_name)
				output_file.write(line)


output_file.close()
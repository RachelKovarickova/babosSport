# f = open('upravenaprvniverze.csv', 'r')

output_file = open("category.csv", "w")

with open ("upravenaprvniverze.csv") as f:
		header = f.readline()
		header_columns = header.split(",")
		order_item_position = header_columns.index('order_item_name')
		month_position = header_columns.index('mesiac')
		timeOfDay_positon = header_columns.index('casovy usek')
		year_position = header_columns.index('rok')
		dayOfWeek_position = header_columns.index('den v tyzdni')
		zip_position = header_columns.index('billing_zip')
		date_position = header_columns.index('created_on')
		#print(order_item_position)

		category = {
			"bunda" : "odev",
			"triko" : "odev",
			"kalhoty" : "odev",
			"vesta" : "odev",
			"návleky" : "odev",
			"obuv" : "obuv",
			"boty" : "obuv",
			"batoh" : "doplnky",
			"ponožky" : "odevni doplnky",
			"rukavice" : "odevni doplnky",			
			"trenýrky" : " odevni doplnky",
			"pouzdro" : "doplnky",
			"světlo" : "doplnky",
			"pás" : "doplnky",
			"čepice" : "odevni doplnky",
			"balzám" : "doplnky",
			"láhev" : "doplnky",
			"tkaničky" : "doplnky",
			"šátek" : "doplnky",
			"podprsenka" : "odevni doplnky",
			"tílko" : "odevni doplnky",
			"hřeby" : "doplnky",
			"čelenka" : "odevni doplnky",
			"poukaz" : "doplnky",
			"tretry" : "obuv",
			"klíč" : "doplnky",
			"košilka" : "odev",
			"kalhotky" : "odevni doplnky",
			"ledvinka" : "doplnky",
			"mikina" : "odev",
			"vak na vodu" : "doplnky",
			"čelenky" : "doplnky"
 			}
		

		output_line = []
				
		output_line.append("month")
		output_line.append("timeOfDay")
		output_line.append("dayOfWeek")
		output_line.append("year")
		output_line.append("categoryName")
		output_line.append("orderItem")
		output_line.append("counter")
		output_line.append("Date")
		output_line.append("zip")
		output_line.append("\n")


		output_file.write(",".join(output_line))
		
		counter = 0

		for line in f:

			column = line.split(",")
			order_item_name = column[order_item_position]
			item_found = 0
			

			for item_name in category:
				
				if order_item_name.find(item_name) > -1:
					item_found = 1
					category_name = category[item_name]
					#print(category[item_name])
					#print(order_item_name)

			"""if item_found == 0:
													print(order_item_name)
													counter += 1
												if counter == 20:
													break"""


			if item_found == 1:
				output_line = []
				
				output_line.append(column[month_position])
				output_line.append(column[timeOfDay_positon])
				output_line.append(column[dayOfWeek_position])
				output_line.append(column[year_position])
				output_line.append(category_name)
				output_line.append(column[order_item_position])
				output_line.append("1")
				zip = column[zip_position].replace(" ", "").strip()
				output_line.append(column[date_position])

				if len(zip) == 5:
					output_line.append(zip)
				else:
					output_line.append("")

				output_line.append("\n")

				output_file.write(",".join(output_line))
output_file.close()


				


	

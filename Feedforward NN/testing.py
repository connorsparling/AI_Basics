import csv

RELEVANT_COLUMNS = ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "Age_Mons", "Qchat-10-Score", "Sex", "Ethnicity", "Jaundice", "Family_mem_with_ASD"]

with open("ToddlerAutism.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers_row = next(csv_reader)
    y_index = headers_row.index("Class/ASD Traits")
    print(headers_row[y_index])
    

    headers = [h for h in headers_row if h in RELEVANT_COLUMNS]


    # for row in csv_reader:
    #     dp = [row[i] for i in range(len(headers_file)) if headers_file[i] in RELEVANT_COLUMNS[subset]]
    #     X.append(dp)
    #     y.append(row[y_index])
csv_file.close()
#read student data from a CSV file
def extract_student_data(student_file):

    with open(student_file, "r") as file:
        
        data = file.readlines()

    return data

raw_data = extract_student_data("students_raw.csv")
print(raw_data)
#remove header
records = raw_data[1:]
for r in records:
    print(r.strip())

#transform student data into a list of lists
rows = []

for r in records:
    columns = r.strip().split(",")
    columns[1] = columns[1].strip()
    if columns[3] == "" or columns[3] == "absent":
        columns[3] = "0"
    marks = int(columns[3])
    if marks < 40:
        result = "Fail"
    else:
        result = "Pass"
    columns.append(result)
    rows.append(columns)

print(rows)

with open("students_clean.csv", "w") as file:
    file.write("student_id,name,department,marks,result\n")  # header

    for row in rows:
        line = ",".join(row)
        file.write(line + "\n")

print("ETL pipeline completed. File saved as students_clean.csv")

# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("please enter the file name:")
# open the file
# Worksheet 1.3: Task 3
output_filename = filename + "_out.csv"

with open(filename, "r") as infile, open(output_filename, "w") as outfile:
    for line in infile:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split(",")
        student_id = parts[0]
        
        scores = [float(x) for x in parts[1:] if x.strip() != ""]
        
        # 计算平均分
        if len(scores) > 0:
            avg = sum(scores) / len(scores)
        else:
            avg = 0.0
            

        if avg >= 70:
            classification = "1"
        elif avg >= 60:
            classification = "2:1"
        elif avg >= 50:
            classification = "2:2"
        elif avg >= 40:
            classification = "3"
        else:
            classification = "F"
            
        outfile.write(f"{student_id},{avg:.2f},{classification}\n")

print(f"Done! Check {output_filename}")

# read in the data, and for each student calculate their average grade and classification



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder
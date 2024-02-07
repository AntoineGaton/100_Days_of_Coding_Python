line = "======================================================================================================================================================"

# Open the source file in read mode
with open('project_euler_algos.txt', 'r', encoding='utf-8') as source:
    # Open the destination file in write mode
    with open('destination_file.txt', 'w', encoding='utf-8') as destination:
        # Iterate over each line in the source file, with line enumeration starting at 1
        for i, line in enumerate(source, start=1):
            # Check if it's the second line
            if i == line:
               
                # Write the second line to the destination file
                destination.write(line)
                # Optionally, break after copying the line to stop reading the source file
                break

print('The second line has been copied from source_file.txt to destination_file.txt')

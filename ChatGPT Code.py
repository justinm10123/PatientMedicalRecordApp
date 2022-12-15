import os

# path to the folder containing the text files
folder_path = '/path/to/folder/'

# open the first text file and read each line
with open(os.path.join(folder_path, 'file1.txt'), 'r') as file1:
    for line in file1:
        # split the line into words
        words = line.split()
        if len(words) > 0:
            # get the first word from the line
            first_word = words[0]

            # open the second text file and read each line
            with open(os.path.join(folder_path, 'file2.txt'), 'r') as file2:
                for line2 in file2:
                    # split the line into words
                    words2 = line2.split()
                    if len(words2) > 0:
                        # get the first word from the line
                        first_word2 = words2[0]

                        # if the first words match, append the second line to the first line
                        if first_word == first_word2:
                            line += line2
                            break

        # write the updated line to the first text file
        with open(os.path.join(folder_path, 'file1.txt'), 'w') as file1_updated:
            file1_updated.write(line)

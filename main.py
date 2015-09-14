import re
import time
import os
import encodings

TRAINING_DIR = 'training'
TEST_DIR = 'test'
TRAINING_DIR_DOT = 'training/dot'
TEST_DIR_DOT = 'test/dot'

start_time = time.time()
list_of_filename = os.listdir(TEST_DIR)
count_file = 0

if not os.path.exists(TEST_DIR_DOT):
    os.makedirs(TEST_DIR_DOT)

for filename in list_of_filename:
    filePath = TEST_DIR + "/" + filename
    savePath = TEST_DIR_DOT + "/" + filename
    count_file += 1
    print('File Name: ', filename)
    with open(filePath, encoding = "ISO-8859-1") as input_file, open(savePath, 'w') as output_file:
        firstLine = next(input_file)
        input_file.seek(0)
        for line in input_file:
            if line == firstLine:
                output_file.write(line + ".")
            else:
                output_file.write(line)
    input_file.close()
    output_file.close()



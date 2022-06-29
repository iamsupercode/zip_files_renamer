"""
    A simple script to unzip files and rename them removing a specified key

    My use case is removing the tags on mp3 files downloaded from external sources such as HipHopKit

    By Yours Truly: SuperCode
"""

import glob
import os
import sys
import zipfile
from loguru import logger

input_directory = sys.argv[1]
output_directory = sys.argv[2]

value_to_be_replaced = input('Type in the value to be replaced: ')
value_to_be_placed = input('Type in value to replace with: ')

# list all zip files
zip_file_paths = glob.glob(input_directory + '*.zip')

# unzip each file
for zip_file in zip_file_paths:
    # unzip contents to output directory
    with zipfile.ZipFile(zip_file, 'r') as zip_file_reference:
        logger.info(f'Unzipping {zip_file}')
        zip_file_reference.extractall(output_directory)

# Walk the output directory renaming files removing specified keyword
for root, directories, files in os.walk(output_directory, topdown=False):
    for filename in files:
        # check if value to be removed is in the filename else continue
        if value_to_be_replaced in filename:
            # rename the file
            new_filename = filename.replace(value_to_be_replaced, value_to_be_placed)
            source = os.path.join(root, filename)
            destination = os.path.join(root, new_filename)
            os.rename(source, destination)
            logger.success(f'Renamed: {filename} -> {new_filename}')
        else:
            # proceed to the next iteration
            continue

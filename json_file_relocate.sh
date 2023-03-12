#!/bin/bash

# Source directory where the JSON files are located
src_dir="/path/to/source/directory"

# Destination directory where the JSON files will be moved to
dest_dir="/path/to/destination/directory"

# Move all the JSON files from the source directory to the destination directory
mv "${src_dir}"/*.json "${dest_dir}"

# To run this script every hour, add the following line to your CronTab:
# 0 * * * * /path/to/script.sh

# Explanation of CronTab syntax:
# - The first field specifies the minutes when the command should be run (in this case, "0" for the start of the hour)
# - The second field specifies the hour when the command should be run (in this case, "*" for every hour)
# - The remaining fields specify the day of the month, month, and day of the week (in this example, all set to "*")
# - The final field specifies the command to run (in this case, the full path to the script file)

# To edit your CronTab, type the following command in your terminal:
# crontab -e

# This will open your CronTab file in your default text editor.
# Add the following line to the file and save it:
# 0 * * * * /path/to/script.sh

# This will run the script every hour on the hour. You can adjust the timing as needed by changing the first two fields of the CronTab entry.

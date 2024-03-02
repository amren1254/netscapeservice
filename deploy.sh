#!/bin/bash

# Script to transfer a zip file to a specific directory on a remote server using scp

# Local file path
local_file="/home/anuj/anuj/mysite/file.zip"

# Remote server details
remote_user="root"
remote_ip="139.59.233.59"
remote_directory="/root/netscape-new-website"

# Transfer the file using scp
scp "$local_file" "$remote_user@$remote_ip:$remote_directory"

# Check if the scp command was successful
if [ $? -eq 0 ]; then
    echo "File transferred successfully."
else
    echo "Error: File transfer failed."
fi

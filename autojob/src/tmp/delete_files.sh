#!/bin/bash

# Specify the directories to delete files and subdirectories from
directories=("all_postings" "job_posts" "keywords_results" "preprocessed_files")

# Function to recursively delete files and directories
delete_contents() {
    local dir="$1"
    if [ -d "$dir" ]; then
        echo "Deleting contents in $dir..."
        rm -rf "$dir"/*
        echo "Contents in $dir deleted successfully."
    else
        echo "Directory $dir not found."
    fi
}

# Loop through each directory and call the function to delete contents
for dir in "${directories[@]}"; do
    delete_contents "$dir"
done

echo "Script execution complete."

#!/bin/bash

# Check if two arguments are provided
if [ $# -eq 2 ]; then
  # Assign the arguments to variables
  dir=$1
  branch=$2
  # Change to the specified directory
  cd ../$dir
  # Check if the directory is a git repository
  if [ -d .git ]; then
    # Pull the specified branch from the remote repository
    git pull origin $branch &
    # git status
    # git branch
    # Wait for the git process to finish
    wait $!
    echo -e "\nFinished the process of 'git pull' on branch '$branch' from repo '$dir'."
    echo -e "Please review this output & adjust accordingly"
  else
    # Print an error message if not a git repository
    echo "$dir is not a git repository"
  fi
else
  # Print an error message if not enough arguments are provided
  echo "Please provide a directory and a branch as arguments"
fi
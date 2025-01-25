#!/bin/sh

# Adding Commit Message
read -p "Add Git Commit Message:" gitcommsg

# Change directory
cd ~/Documents/Code/Modern_Phy_Lab

# Add all files to git
git add .

# Add a commit Message from stored variables
git commit -m "$gitcommsg"

# Pushing the commit
git push -u origin main



# TimeTrackerGUI
A simple GUI time tracker using Python and tkinter. Exports times to .txt file for archival purposes. 
I made this in order to keep track of my hours working on projects.
Uses datetime.timedelta() to calculate total time.

# save
saves a recording of the date, start time, end time, and total time to .txt in root folder.
Each time recording is saved in this format: 
```
Date, Start, End, Total, *Note
```
Easy to convert to CSV file for use in Excel

# issues
- antivirus can cause problems with writing to .txt file. Disable AV in source folder
- timer does not count over 24 hours, though no one should be working that long


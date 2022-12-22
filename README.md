# Submission Helper

This tool is helping vfx vendors to send media to productions or other studios.

Each sending usually consists of one or more media files, together with spreadsheet that binds the media files with additional info like notes, status, version, task...

This process doesn't seem to have an industry standard, Submission Helper has numerous options to help interface vendor and production with as little friction as possible.

Here is the overview from ShotGrid:
https://knowledge.autodesk.com/support/shotgrid/getting-started/caas/CloudHelp/cloudhelp/ENU/SG-Tutorials/files/SG-Tutorials-tu-submission-overview-html-html.html

## Intended use
Package starts with one or more files that you want to package and send. Submission Helper checks all the files and helps to produce spreadsheet(s) and email that is easily ingested in receiver's system, often automatically.

## Features:
* Helps to name the package by the template, including consecutive or per day versions
* Reads metadata from the files by ffprobe and other methods
* Calculates file sizes
* Allows to gather and copy sidecar files like CDLs or LUTs to the package.
* Allows to define spreadsheet columns and values in a flexible way
* Generates up to two spreadsheets that are called in gui submission and drive log
* Generates a text file that is often used for email that follows up the sending.
* Can read notes from Ftrack
* Allows for checking for holes in file sequences, files with zero size and other common problems
* Allows saving config to json files
* Can be used head-less 

## Quick How-to
Submission Helper assumes you put the file(s) in one folder - the Package Folder.

1. Drag the package folder path to the Package Folder
2. Set the Package Name options, till the preview matches what you need
3. Use Spreadsheet tab to define columns and their values
4. Set the export options in Exports and text tabs
5. Press Go to export
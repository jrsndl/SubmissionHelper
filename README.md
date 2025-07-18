# Submission Helper

This tool is helping vfx studios to share and ingest data.

Each sending usually consists of one or more files, together with a spreadsheet that binds the media files with additional info like notes, status, version, task...

This process doesn't seem to have an industry standard; Submission Helper has many options to help interface vendor and production with as little friction as possible.

Here is the overview from ShotGrid:
https://help.autodesk.com/view/SGSUB/ENU/?guid=SG_Tutorials_tu_submission_overview_html

## Tasks

You have a bunch of files, often images, sequences or movies, or project files.

**If it is your studio output:**
* You want to check if the files match the resolution, frame rate, metadata, naming and other requirements of your client.
* You might want to check and share the lenght, status or other info stored in your asset management system with your client.
* Your client might require a spreadsheet with summary of the files your sending in very specific format.
* You might want to share a thumbnail for every shot you are sharing with your client.
* You might want to collect and add files connected with your sending, like per shot LUTs.
* You might need to rename files from your naming convention to something client requires.

**If it is an input for your studio, you might want to ingest it to Ayon pipeline.**
* You can check and generate Ayon csv ingest and send your ingest to Deadline farm.
* You can also read a spreadsheet from your vendor and use the data for your ingest.


Submission Helper (SH) inspects the image files using ffprobe and oiiotool. It also does basic parsing of Nuke scripts and Maya scenes.

SH can use a spreadsheet file with arbitrary data as a source of truth, as well as ftrack and Ayon database.

SH can export Spreadsheet in three forms, named Submission, Drive Log and Text. This naming was picked a long time ago, originally for submission to contain client data, drive log to contain a record of what was sent, and text file to help making a summary email.

SH relies on the idea that files have some naming convention that allows to parse the metadata and possibly linking it to a database.

## Intended use
Package starts with one or more files that you want to package and send. Submission Helper checks all the files and helps to produce spreadsheet(s) and email that is easily ingested in receiver's system, often automatically.

## Features:
* Helps to name the package by the template, including consecutive or per day versions
* Reads metadata from the files by ffprobe, oiiotool and other methods.
* Calculates file sizes.
* Allows gathering and copying sidecar files like CDLs or LUTs to the package.
* Allows defining spreadsheet columns and values in a flexible way.
* Generates up to two spreadsheets that are called submission and drive log.
* Generates a text file often used for email that follows up the package sending.
* Can read notes and other data from the ftrack.
* Can read info from Ayon database.
* Allows for checking for holes in file sequences, files with zero size and other common problems
* Allows saving the ui as a json settings file.
* Can be used head-less.

## Quick How-to
Submission Helper assumes you put the file(s) in one folder - the Package Folder.

1. Drag the package folder path anywhere to the Submission Helper window
2. Set the Package Name options, till the preview matches what you need
3. Use Spreadsheet tab to define columns and their values
4. Set the export options in Exports and text tabs
5. Press Go to export

## Keywords

Many SH operations produce or link keywords to files in the package. Use the Inspector tab to check and search keywords.

Some keywords are metadata processed by SH, like timecode for the middle frame of the current video, or Nuke file sequence notation.   

name: file name, no path, no extension
printf_pattern: file name, for file sequence number is replaced with %04d for 0001
sequence_nuke: file name, number for file sequence is replaced by [start..end]
sequence_slate
sequence_slate_nuke
clean_name: file name with no extension and no trailing number
clean_name_no_sep: file name with no extension and no trailing number, if there is dot underscore or dash before trailing number, it is removed
clean_name_sep_char: the number separation character

number: trailing number
start_number: first number in file sequence
end_number: last number in file sequence
padding: leading zeroes used for trailing number
range: start-end frames for file sequence
range_slate: same as range, start+1

extension: file extension, no dot

path_prs: path, with no file, no trailing slash
full_path: path to the file or first frame in file sequence
relative_path: path to the file, minus the path start to the package. Starts with slash
drive: drive letter (windows)

size_bytes: file size in bytes, calculated as total for file sequence
size_human: same as size_bytes, rounded to one decimal, with units

category: files are categorized by extension. still, sequence, video, audio, multiframe, other

cnt_sub, cnt_log, cnt_txt: counter for each export
total_sub, total_log, total_txt: total number of files for each export
files_sub, files_log, files_txt: total files for each export

d, dd, y, yy, m, mm: today day, month and year
package_date: package renaming date 
package_name: package renaming name
package_version: package renaming version
package_name_from_folder: folder name initially provided by user
package_name_root: path to the package, without end folder

meta_aspect: image aspect, float
meta_aspect_x: 
meta_aspect_y:
meta_audio_present
meta_audio_present
meta_audio_present
meta_bits_per_sample_audio
meta_channels_audio
meta_codec_long_name_audio
meta_codec_long_name_video
meta_codec_name_audio
meta_codec_name_audio
meta_data_present
meta_duration_audio
meta_duration_frames
meta_duration_frames_slate
meta_duration_secs
meta_fields
meta_fps
meta_fps_a
meta_fps_a
meta_fps_raw
meta_frame_end_from_tc
meta_frame_end_from_tc_slate
meta_frame_start_from_tc
meta_frame_start_from_tc_slate
meta_height
meta_is_log
meta_reel
meta_sample_rate_audio
meta_time_code
meta_time_stamp_audio
meta_time_stamp_video
meta_video_present
meta_width




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

1. Drag the package folder path anywhere to the Submission Helper window
2. Set the Package Name options, till the preview matches what you need
3. Use Spreadsheet tab to define columns and their values
4. Set the export options in Exports and text tabs
5. Press Go to export

## Keywords

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




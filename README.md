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

## Installation

Submission Helper needs Python 3.10 (PySide2 has no wheels for newer Python).
With [uv](https://docs.astral.sh/uv/):

```powershell
uv venv --python 3.10
uv pip install -r requirements.txt
uv run python submission_helper.py
```

ffprobe and oiiotool are external tools. They are found on `PATH`, through
`install.json`, or through the `SH_FFPROBE` / `SH_OIIOTOOL` / `SH_FFMPEG`
environment variables. oiiotool for Windows is included in `oiio/win`.

## Building the exe

Run `build_exe.bat` (needs [uv](https://docs.astral.sh/uv/)). It creates
`.venv` if needed, installs the requirements and PyInstaller, and builds
`dist\SubmissionHelper\`:

| File | Use |
|---|---|
| `SubmissionHelper.exe` | the GUI, no console window |
| `SubmissionHelper-cli.exe` | the same app with a console: headless / command line runs and log output |

The `oiio`, `ocio` and `ffmpeg` folders and `install.json` / `default.json`
are copied next to the exes, where the app looks for them. Zip the whole
`dist\SubmissionHelper` folder to share it; check `install.json` for API keys
first. Console tools the app runs (ffprobe, oiiotool, converts, ayon) don't
open console windows.

## Command line

Without arguments Submission Helper opens the GUI. Given both `-i` and `-p`
it runs **headless**: it loads the preset, runs the `--actions` in order,
writes its log to the console and exits. This is meant for automation, for
example a farm job or a watch-folder script.

```
python submission_helper.py [-h] [-i PATH] [-p PRESET] [--actions LETTERS]
                            [--settings KEY=VALUE[,KEY=VALUE...]]
```

With the built executable use `SubmissionHelper-cli.exe` instead of
`python submission_helper.py` (the windowed `SubmissionHelper.exe` has no
console to print to). Run with `-h` to print the help.

| Option | Meaning |
|---|---|
| `-i`, `--input PATH` | Package folder, or a csv file inside it. With *Vendor → Auto Detect* on in the preset, the csv is used as the vendor csv. |
| `-p`, `--preset PRESET` | Preset json file, or the name of a saved preset (without `.json`), looked up in the same places as the GUI preset list. |
| `--actions LETTERS` | Actions to run, left to right. Default `ftg`. |
| `--settings KEY=VALUE,...` | Override preset values for this run only. |
| `-v`, `-q`, `--log-level`, `--log-file` | Console log level and log file, see [Logging](#logging). |

### Actions

| Letter | Action | What it does |
|---|---|---|
| `f` | Read files | Scan the package folder, read metadata and csv / Ayon / ftrack data |
| `t` | Transform data | Apply parsing, spreadsheet columns, naming and checks |
| `d` | Reload | Same as `f` + `t`. Use it after `r` or `c`, which change files on disk |
| `g` | Go | Same as the **Go** button: export submission, drive log and text as set in the preset. Also copies sidecar files (*Copy with Go*), runs converts (*Convert on Go*) and renames the package folder (*Auto Rename*) when those are on |
| `s` | Sidecar files | Copy sidecar files to their destinations |
| `r` | Rename | Rename / move files using the Rename tab rules |
| `c` | Convert | Run the Convert tab commands |
| `p` | Publish to Ayon | Export the submission csv and ingest it to Ayon locally |
| `P` | Publish to Ayon (farm) | Same as `p`, submitted as a Deadline job |
| `a` | Ayon shot list | Read, filter and write the Ayon shot list (Ayon tab) |
| `x` | ftrack shot list | Write `ftrack_shotlist.csv` next to the package |

Most actions work on data prepared by `f` and `t`, so start with `ft`.
Spreadsheets and text are **only** exported by `g`; a run without `g`
exports nothing (useful for rename-only or publish-only jobs).

Typical sequences:

| `--actions` | Result |
|---|---|
| `ftg` | Check the package and export (default) |
| `ftrdg` | Rename files, re-read them, export |
| `ftrdsg` | Rename, re-read, copy sidecars, export |
| `ftp` / `ftP` | Publish to Ayon locally / on the farm (writes only the submission csv it ingests) |
| `a` | Export the Ayon shot list only |

### Overriding preset values

`--settings` takes comma separated `key=value` pairs. Keys are the setting
names used in the preset json (open a saved preset to see them, e.g.
`name_rename_auto`, `prefs_counter_start`). Values are converted by the type
of the setting:

* checkboxes and radio buttons: `true` / `false` (also `1`/`0`, `yes`/`no`, `on`/`off`)
* number fields: integers
* text fields: the text as is

Unknown keys and values that don't fit the type are skipped with a warning.
Values can't contain commas.

### Examples

```powershell
# check a package and export, preset given as a file
python submission_helper.py -i D:/out/pkg_v001 -p D:/presets/clientX.json

# the same with a saved preset name
python submission_helper.py -i D:/out/pkg_v001 -p clientX

# rename, re-read, copy sidecars, export
python submission_helper.py -i D:/out/pkg_v001 -p clientX --actions ftrdsg

# export without renaming the package folder, start the counter at 5
python submission_helper.py -i D:/out/pkg_v001 -p clientX --settings name_rename_auto=false,prefs_counter_start=5

# vendor delivery: the csv sets the package folder and is used as vendor csv
python submission_helper.py -i D:/in/vendor_0412/delivery.csv -p ingest_vendor
```

### Exit codes

| Code | Meaning |
|---|---|
| `0` | Finished |
| `1` | Input or preset not found, or an action crashed |
| `2` | Bad arguments: only one of `-i` / `-p`, or an unknown action letter |

Many problems (a file that can't be read, a failed export) are logged but
don't stop the run, so check the log output, not only the exit code.

On Linux without a display (render nodes), headless mode switches Qt to
the `offscreen` platform automatically.

## Ayon shot list and versions

The **Ayon** tab reads the folders (shots, assets) and tasks of an Ayon
project. Rows are matched to the package files with the matching rules, and
their values become keywords with the Ayon prefix, e.g. `{ayon_Folder Path}`.

* **Scan** reads the list now. It works without a loaded package, and also
  when *Enable* is off (that checkbox controls reading on package load).
* **List Filters** limit the list: Assets / Shots / Tasks / Other, task types,
  **Task Names** (comma separated, wildcards `*` `?`, e.g. `comp*`) and
  assignees. A task row must pass every enabled filter.
* **Export Shot List** writes `ayon-list.csv` (visible rows only) to the output
  folder, and with **Versions CSV** also `ayon-list-versions.csv` (see below).

Columns per row include the frame range (`In`, `Out`, `Head`, `Tail`,
`Range` with handles, `Length`), resolution, `Start Date` / `End Date`
(`YYYY-MM-DD`, task rows use the task's dates), status, assignees and links.

### Pulling versions

Turn on **Pull versions** and set **Product filters** to add version info of
the preferred product to every shot / asset row and its task rows:

```
comp:renderCompMain:exr, :platePl01:exr
```

Each filter is `task:product:representation`:

| Filter | Means |
|---|---|
| `comp:renderCompMain:exr` | representation `exr` of product `renderCompMain`, published from task `comp` |
| `:platePl01:exr` | the same, from any task |
| `platePl01:exr` | the same as above |
| `:platePl01` | any representation |
| `render*:exr` | wildcards `*` `?` in any part, names are not case sensitive |

Filters are tried in order and the first one with a match is used, so put the
preferred product first. The **latest version** of the product is used; if it
doesn't have the representation, that filter doesn't match.

Added columns: `Product`, `Product Type`, `Version`, `Version Name` (`v007`),
`Version Status`, `Version Author`, `Version Date`, `Version Comment`,
`Version Task`, `Representation`, `Repre Path`, `Version Filter`, and from
the version's attributes and data: `Version Frame Start`, `Version Frame End`,
`Version Handle Start`, `Version Handle End`, `Version FPS`, `Version Width`,
`Version Height`, `Version Pixel Aspect`, `Version Step`, `Version Host`,
`Version Colorspace` (taken from the representation when the version doesn't
have it). With the default prefix they are available as `{ayon_Version}`,
`{ayon_Version FPS}`...

Versions are read with three queries for the whole project. Changing the
filters takes effect with the next **Scan** or package load.

### Matched Versions

With **Pull versions** on and package files matched to Ayon folders (*Match
Package Keys to Shot List Keys*), the **Matched Versions** sub-tab lists all
versions of the configured products (the product filters: product name, task
and representation must fit) of the matched folders only, sorted by folder
path and then version. The version picked by the filters as the preferred one
is marked `Preferred` and highlighted.

Columns: `Folder Path`, `Folder Name`, `Folder Type`, `Product`,
`Product Type`, `Version`, `Version Exists` (`True` when a package file has
this version, see Match version), `Max Existing Version` (highest version of
the product in the folder), `Version Name`, `Preferred`, `Version Status`,
`Version Author`, `Version Date`, `Version Comment`, `Version Task`,
`Representations` (all representation names), and the version attribute /
data columns listed above.

Ayon is asked again only when the matched folders or the product filters
change, not on every edit. Turn on **Versions CSV** to also write the list to
`ayon-list-versions.csv` with **Export Shot List**.

**Show matched only** (above the table) shows just the versions a package
file matched (teal, see Match version). The list filters apply here too:
versions of folders hidden in the Shot List are not shown.

Both csv files contain exactly what the tables show: `ayon-list.csv` follows
the list filters and **Matched Only**, `ayon-list-versions.csv` follows the
list filters and **Show matched only**.

### Matching a version to each file

**Match version** (second row of the Versions group) finds, for every file
matched to an Ayon folder, the Matched Versions row of the same folder where
the **Package** key equals the **Version** key:

| Package | Version | Matches |
|---|---|---|
| `{version}` | `{Version}` | file version `007` to Ayon version `7` (numbers compare by value) |
| `v{version}` | `{Version Name}` | `v007` to `v007` |

The row's columns are added to the file with the Ayon prefix and `Matched`,
for example `{ayon_Matched Version}`, `{ayon_Matched Version Status}`,
`{ayon_Matched Version Comment}`, `{ayon_Matched Repre Path}`. When several
products have the same version number, the preferred product wins. Matched
rows are teal in Matched Versions and the `Matched Files` column counts the
files.

For checks, every file matched to an Ayon folder also gets
`{ayon_Matched Version Exists}` (`True` / `False`: is the file's version
already in Ayon) and `{ayon_Matched Max Existing Version}` (highest existing
version of the preferred product), also when its version is not in Ayon yet. Changing these keys doesn't query Ayon again. When some files don't
find their version, the Log tab shows what was compared.

## Logging

Everything Submission Helper does is logged with a level:

| Level | Used for |
|---|---|
| `DEBUG` | Details: every renamed frame, every metadata read, commands that are run |
| `INFO` | What happened: files scanned, spreadsheets written, files renamed, sidecars copied |
| `WARNING` | Something to check: missing ffprobe, a rename skipped because the destination exists |
| `ERROR` | Something failed: an export could not be written, a publish failed |

Messages from Qt itself (for example image or font warnings) are logged too,
under the name `Qt`, and unexpected crashes are logged as `CRITICAL` with the
full traceback.

### Log tab (GUI)

The **Log** tab shows the log of the current session. Its title counts
warnings and errors, e.g. `Log (1 err, 3 warn)`, and turns orange or red, so
you can see a problem without opening the tab.

* **Show** – minimum level to display. Everything is recorded, so switching to
  `DEBUG` also shows debug messages logged earlier. The choice is saved with
  the GUI settings.
* **Filter text** – show only lines containing the text.
* **Auto-scroll** – keep the newest line in view.
* **Copy** / **Save...** – copy or save the lines currently shown.
* **Clear** – empty the log and reset the counters.

The tab keeps the last 20,000 lines.

### Console and log file

The console (stderr) gets the log in GUI and headless mode. Its level is set
on the command line and is independent of the Log tab:

| Option | Console output |
|---|---|
| *(default)* | `INFO` and above |
| `-v`, `--verbose` | `DEBUG` and above |
| `-q`, `--quiet` | `WARNING` and above |
| `--log-level LEVEL` | `debug`, `info`, `warning`, `error`, or `none` for no console output |
| `--log-file PATH` | Also append the full log (all levels, with date and thread) to `PATH` |

```powershell
# farm job: only problems on the console, everything in a file
python submission_helper.py -i D:/out/pkg_v001 -p clientX -q --log-file D:/logs/pkg_v001.log

# debugging a preset in the GUI
python submission_helper.py -v
```

A headless run ends with a summary line such as
`Headless run finished: 0 error(s), 2 warning(s).`

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




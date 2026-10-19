"""
Tooltips for the main window controls.

All GUI tooltips live here instead of in submission.ui, so they can be
reviewed in one place and are not lost or copy-pasted between controls in
Qt Designer. ``apply_tooltips(ui)`` is called once after ``setupUi``.

Keys are widget objectNames. Numbered rows (parse_name_01..48, check_if_01..21,
...) share one text through ``ROW_TOOLTIPS`` (regex on the objectName).

Widgets built in code (submission_helper.py: _add_ayon_controls, the panel
splitter, log_view.py) set their own tooltips where they are created, and
ayon_output_folder gets its tooltip there too.

Texts are plain text; ``\\n`` is a line break. They are converted to Qt rich
text when applied, so ``<`` and ``>`` are safe to use.

A control that is in the GUI but not read by the code yet ends its tooltip
with ``NOT_IMPLEMENTED``. Remove that suffix when the feature is added.
"""
import html
import re

NOT_IMPLEMENTED = "\n(Not implemented yet.)"

_SHOW_TAB = "Show this tab.\nHiding a tab does not switch its features off."

TOOLTIPS = {
    # ------------------------------------------------------------ main window
    "write_button":
        "Export the spreadsheets and text set on the Exports tab.\n"
        "Also copies sidecars (Copy with Go), runs converts (Convert on Go)\n"
        "and renames the package folder (Auto Rename) when those are on.\n"
        "Uses the data currently shown: press Reload first if files changed.",
    "reload":
        "Rescan the package folder: files, sizes, metadata and CSV data.\n"
        "Use after files changed on disk, after loading a preset,\n"
        "or after changing Frame Rate / OCIO on the Preferences tab.",
    "publish_local_button":
        "Write the Submission spreadsheet and ingest it into Ayon on this machine.\n"
        "Needs a loaded package, Project (Ayon tab), Folder and Task\n"
        "(Ayon Publish tab), Exports > Submission > CSV on, and the ayon path.\n"
        "Each split file is published. The window waits until it finishes.",
    "publish_farm_button":
        "Write the Submission spreadsheet and submit its Ayon ingest as a\n"
        "Deadline job. Needs a loaded package, Project (Ayon tab), Folder and\n"
        "Task (Ayon Publish tab), Exports > Submission > CSV on, and the ayon\n"
        "and deadlinecommand paths. Pool, group etc. come from Ayon Publish.",
    "progressBar":
        "Metadata reading progress of the last load / Reload.",

    # ------------------------------------------------------------ Package tab
    "package_folder":
        "Folder with the package files (scanned with all subfolders).\n"
        "A file path uses the file's folder. A .csv also becomes the\n"
        "Vendor CSV when Vendor > Auto Detect is on.\n"
        "Every change rescans: paste, browse or drop a path instead of typing.",
    "package_explore":
        "Open the package folder in the file manager.",
    "package_browse":
        "Pick the package folder and scan it.",
    "age_enabled":
        "Keep only recently written files in the Submission.\n"
        "Older items are hidden from the Submission (Drive Log and Text\n"
        "keep them). A sequence counts as old as its newest frame.",
    "age_number":
        "Age limit. Items older than this are hidden from the Submission.",
    "age_unit":
        "Unit of the age limit.",
    "age_type":
        "File time used for the age test.\n"
        "created = creation time on Windows; on Linux/macOS it is the\n"
        "time the file's metadata last changed.",
    "age_exclude":
        "Never hide these files by age.\n"
        "Words matched anywhere in the file path, separated by spaces.\n"
        "Plain text, case-sensitive. Example: _slate .cube",
    "age_include":
        "Apply the age filter only to files whose path contains one of\n"
        "these words (separated by spaces). Plain text, case-sensitive.\n"
        "Empty: the age filter applies to all files.",
    "name_template":
        "Name for the package folder when Name From is Template.\n"
        "Tokens: {yy} {y} {mm} {m} {dd} {d} (today) and {package_version}\n"
        "(the next free version). No other tokens are allowed.\n"
        "Example: sub_{yy}{mm}{dd}_{package_version}",
    "name_date_regex":
        "Regex that finds the date stamp: capture group 1, or the whole\n"
        "match when there is no group. Run on the expanded Template (today's\n"
        "date) and on the names of the folders next to the package.\n"
        "Date tokens {yy} {mm} {dd}... are expanded, so the default\n"
        "sub_{yy}{mm}{dd} finds today's packages.",
    "name_version_regex":
        "Regex that finds the version in the names of the folders next to\n"
        "the package; capture group 1 is the version.\n"
        "Numbers: _(\\d{3})$   Letters: _([A-Z])$",
    "name_version_per_date":
        "Restart versions every day (A or 1 for the day's first package).\n"
        "Only folders with today's date (Date Regex) are compared.\n"
        "Off: versions continue across dates. Also sets {package_date}.",
    "name_version_zeroes":
        "Digits of a numeric version, e.g. 3 gives 001.",
    "name_version_use_letters":
        "Use letters A-Z instead of numbers for versions.\n"
        "Version Regex must then capture a single letter.",
    "name_version_letters_uppercase":
        "Upper-case letter versions (A). Off gives lower case (a).",
    "name_from_template":
        "Name the package by the Template, with the next free version.",
    "name_from_folder":
        "Keep the current folder name as the package name.\n"
        "Rename and Auto Rename do nothing.",
    "name_rename":
        "Rename the package folder to the Preview name now and reload it.\n"
        "Template mode only.",
    "name_rename_auto":
        "Rename the package folder to the Preview name after Go has exported.\n"
        "Template mode only. Browse to the renamed folder afterwards.",
    "name_preview":
        "Package name that Rename / Auto Rename will use.\n"
        "Available as {package_name}.",

    # ------------------------------------------------------------ Sidecar tab
    "side_folder":
        "Folder searched (with subfolders) for sidecar files: CDL, LUT...\n"
        "Empty: no sidecar search.",
    "package_explore_2":
        "Open the Search Folder in the file manager.",
    "package_browse_2":
        "Pick the Search Folder.",
    "side_exclude":
        "Ignore found files whose full path contains any of these words.\n"
        "Separated by spaces; plain text, case-sensitive.\n"
        "Example: _old .tmp",
    "side_include":
        "Use only found files whose full path contains one of these words.\n"
        "Separated by spaces; plain text, case-sensitive. Empty: all files.\n"
        "Example: .cdl .cc",
    "side_copy":
        "Copy the files listed in the bottom Sidecar Files tab now.\n"
        "Creates missing folders and overwrites existing files.",
    "side_copywithgo":
        "Also copy the sidecar files when Go is pressed.",
    "side_sub_only":
        "Match sidecars only to files shown in the Submission.",
    "side_log_only":
        "Match sidecars only to files shown in the Drive Log.",
    "side_all":
        "Match sidecars to all package files.",

    # ------------------------------------------------------------ Rename tab
    "Rename_go":
        "Rename / move the files listed in the bottom Rename tab now.\n"
        "No undo. Files whose destination exists are skipped.\n"
        "Turn on Reload after Rename to see the new paths right away.",
    "rename_reload_after":
        "Reload the package after Rename, so the tables show the new paths.",

    # ------------------------------------------------------------ Data tab
    "data_enable":
        "Load the Data CSV and pair its rows with the package files.\n"
        "Off: no Data CSV tokens are added.",
    "name_date_prefix":
        "Prefix added to every Data CSV column name.\n"
        "Example: column shot gives the token {data_shot}.\n"
        "Use the prefixed names in the Data fields and spreadsheets.\n"
        "Empty: columns keep their names and may overwrite other tokens.",
    "data_csv_path":
        "Data CSV file, or a folder of CSV files. First row = column names.\n"
        "Folder (or Latest in Folder on): the last *.csv by name is used.\n"
        "The used file name is available as {csv_data_file}.",
    "data_csv_browse":
        "Pick the Data CSV file.\n"
        "With Latest in Folder on, pick the folder instead.",
    "data_csv_latest":
        "Use the last *.csv in the folder, sorted by file name.\n"
        "Lets you add data002b.csv next to data002.csv instead of\n"
        "overwriting it. The file name in the path is then ignored.",
    "data_table":
        "Rows of the loaded Data CSV.\n"
        "Green: the row is paired with a package file.",

    # ------------------------------------------------------------ Ftrack tab
    "ftrack_use":
        "Connect to ftrack and read data for each loaded file.\n"
        "Also needed by Export. Server, user and API key come from\n"
        "install.json (or FTRACK_SERVER / FTRACK_API_USER / FTRACK_API_KEY).\n"
        "Slow: set up the rest of the preset with this off first.",
    "ftrack_project":
        "ftrack project full name. Exact, case-sensitive; Active projects only.",
    "ftrack_shot":
        "ftrack shot name of each file, with tokens, e.g. {shot}.\n"
        "Empty: no ftrack lookup.",
    "ftrack_task":
        "ftrack task name under that shot, with tokens, e.g. {task}.\n"
        "Empty: no ftrack lookup.",
    "ftrack_include_2":
        "Only files with these extensions get ftrack notes, e.g. exr, mov\n"
        "Spaces or commas, with or without dot, not case-sensitive.\n"
        "Empty: all files. OpenPype attributes are read for all files.",
    "ftrack_table":
        "One row per loaded file: shot / task / version looked up, Status\n"
        "(ok, task not found, version not found, template not resolved,\n"
        "skipped (extension)...), notes found, the selected note and range.\n"
        "Green: ok. When nothing was queried it says why.",
    "ftrack_do_op":
        "Read the OpenPype frame range and handles of the ftrack shot.\n"
        "Adds {ftrack_op_frame_start}, {ftrack_op_frame_end}, {ftrack_op_range},\n"
        "{ftrack_op_length}, {ftrack_shot_exists}, {ftrack_task_exists}...\n"
        "Needs Use Ftrack, Project, Shot and Task.",
    "ftrack_do_notes":
        "Read the notes of the ftrack task into {ftrack_note}.\n"
        "Narrow them down with Note Label, Version and Note Pattern.",
    "ftrack_label_use":
        "Use only notes that have the ftrack note label in the next field.",
    "ftrack_label":
        "ftrack note label name, exact. Example: For Client",
    "ftrack_version_use":
        "Read notes from the task's asset version with the number in the\n"
        "next field, instead of the task's own notes.",
    "ftrack_version":
        "Version number to match, with tokens, e.g. {version}.\n"
        "Must give a whole number; otherwise the file gets no notes.",
    "ftrack_note_pattern":
        "Regex that picks the notes for {ftrack_note}. Tokens allowed;\n"
        "regex counts like \\d{3} work too.\n"
        "Note Repl empty: keeps every note that contains a match.\n"
        "Note Repl set: the note must match from its start; the result is\n"
        "Note Repl with the groups filled in. Several notes are joined with ;---;",
    "ftrack_note_repl":
        "Result for a matching note, e.g. \\2 for the 2nd group.\n"
        "Starting with lambda runs Python (re.sub on the note).\n"
        "Empty: the whole note is used.",
    "ftrack_export":
        "Write the ftrack shot list (shots and asset builds with path, tasks\n"
        "and links) to the path next to it. Same as command line action x.\n"
        "Needs Use Ftrack and Project; a package only when the path is empty.",
    "ftrack_path":
        "Where Export writes the ftrack shot list: a .csv file, or a folder\n"
        "(ftrack_shotlist.csv is written in it). Empty: the package folder.",

    # ------------------------------------------------------------ Vendor tab
    "vendor_csv_path_detect":
        "When a .csv is loaded as the package path, use it as the Vendor CSV.\n"
        "The package folder becomes the CSV's folder.",
    "vendor_csv_path":
        "Vendor delivery CSV that lists the files to ingest.\n"
        "First row = column names. Loading a preset in the GUI keeps\n"
        "the current path; headless runs use the preset's path.",
    "vendor_csv_explore":
        "Show the Vendor CSV in the file manager.",
    "vendor_csv_browse":
        "Pick the Vendor CSV file.",
    "vendor_csv_package_key":
        "File side of the pairing with vendor CSV rows: text with file\n"
        "tokens, e.g. {name}. Not a regex.\n"
        "A file and a row pair when this equals the Vendor key exactly.",
    "vendor_csv_vendor_key":
        "Row side of the pairing: text with vendor row tokens, e.g.\n"
        "{vendor_Filename}. Use the column names from Spreadsheet\n"
        "Preferences, or {vendor_<Column>} for other columns.",
    "vendor_csv_ignore":
        "Leave files that are not listed in the Vendor CSV out of the\n"
        "Submission. Needs the Vendor CSV and Spreadsheet Preferences.",
    "vendor_csv_ftrack":
        "Cross check the vendor data with ftrack." + NOT_IMPLEMENTED,
    "vendor_csv_skip":
        "Also leave out files whose Skip by value is listed in To Skip.\n"
        "Needs Ignore Items not in CSV on.",
    "vendor_csv_skip_by":
        "Value tested for each file, with tokens, e.g. {shot}.",
    "vendor_csv_skip_what":
        "Values to leave out, separated by spaces. Exact, case-sensitive.\n"
        "Example: sh010 sh020",
    "vendor_csv_prefs_spreadsheet":
        "JSON describing the vendor CSV columns:\n"
        '{"CsvColumn": {"column": "vendor_X", "validate": "regex",\n'
        '               "default": "", "required": true}, ...}\n'
        "column = token name, validate = regex the value must match,\n"
        "default = value when empty or missing, required = column must exist.\n"
        "Columns not listed become {vendor_<Column>}.",
    "vendor_csv_prefs_repres":
        "JSON describing the representations (outputs) of one delivery:\n"
        "merge_repres_by: tokens that group CSV rows into one version,\n"
        "repres: list of outputs with name, extensions, metadata_check...,\n"
        "task_intent_repres: outputs required per task and intent.\n"
        "Problems are reported in {vendor_row_errors}.",

    # ------------------------------------------------------------ Replace tab
    "replace_enable":
        "Load the Search and Replace CSV and preview its rules.",
    "replace_csv_path":
        "CSV with search and replace rules for text files (e.g. .nk).\n"
        "The last *.csv in the file's folder is used.\n"
        "Columns: Extension,Pattern,Search,Replace. One rule per row.\n"
        "Extension without dot, any case, e.g. nk.\n"
        "Pattern: empty for all files, or text the file name must contain\n"
        "(literal, case-sensitive). Search and Replace are literal text.\n"
        "The used file name is available as {csv_replace_file}.",
    "data_csv_browse_2":
        "Pick the Search and Replace CSV.",
    "replace_withgo":
        "Also run the replace when Go is pressed, as its first step.\n"
        "Files are changed in place, without a backup.\n"
        "Don't also press Replace: running twice applies the rules twice.",
    "replace_button":
        "Apply the replace rules to the package files now.\n"
        "Files are changed in place, without a backup: use it on a copy.\n"
        "Pressing it again applies the rules again.",
    "replace_table":
        "Files the replace rules apply to, with their rules.",

    # ------------------------------------------------------------ Convert tab
    "thumbs_make_on_go":
        "Also run the convert commands when Go is pressed,\n"
        "before the spreadsheets are written.",
    "thumbs_convert_now":
        "Run the convert commands now for all package files.\n"
        "Commands run one by one; the window waits until all are done.",
    "thumbs_skip_existing":
        "Don't run a command when its File Name already exists.",

    # ------------------------------------------------------------ Spreadsheet tab
    "sub_columns":
        "Submission columns as  Title = value  separated by commas.\n"
        "Value is text with tokens, e.g.\n"
        "Shot = {shot}, Frames = {range}, Vendor = MyStudio\n"
        "Put a comma after every column, also at the end of a line.\n"
        "No commas or = inside a value. Unknown tokens stay as {token}.\n"
        "Title = *value  makes the column editable in the Submission table,\n"
        "e.g. Notes = *{note}. Edits are exported, Reload drops them.\n"
        "See the Inspector tab for the available tokens.",
    "log_columns":
        "Drive Log columns as  Title = value  separated by commas.\n"
        "Value is text with tokens, e.g. File = {sequence_nuke}, Size = {size_human}\n"
        "Put a comma after every column, also at the end of a line.\n"
        "No commas or = inside a value. Unknown tokens stay as {token}.\n"
        "Title = *value  makes the column editable in the Drive Log table.\n"
        "Edits are exported, Reload drops them.",
    "txt_columns":
        "Text columns as  Title = value  separated by commas.\n"
        "Put a comma after every column, also at the end of a line.\n"
        "No commas or = inside a value.\n"
        "Each file becomes one line of the text; header, footer and\n"
        "separator are set on the Exports tab.",
    "sub_exclude":
        "Leave out files whose full path contains any of these words.\n"
        "Separated by spaces; plain text, case-sensitive. Example: .mov _proxy",
    "sub_include":
        "Use only files whose full path contains one of these words.\n"
        "Separated by spaces; plain text, case-sensitive. Empty: all files.\n"
        "Exclude is applied afterwards.",

    # ------------------------------------------------------------ Checks tab
    "check_sequence_size_consistency":
        "Warn when a frame's file size differs too much from its neighbours.\n"
        "Tune it on the Preferences tab (Scan Sizes group).\n"
        "Reliable for uncompressed sequences only.",
    "check_sequence_holes":
        "Warn about missing frames in file sequences.\n"
        "The bottom Files tab lists the missing frame numbers.",

    # ------------------------------------------------------------ Ayon Publish tab
    "dead_primpool":
        "Deadline pool of the Ayon ingest job.",
    "dead_secpool":
        "Deadline secondary pool of the Ayon ingest job. Empty: not set.",
    "dead_group":
        "Deadline group of the Ayon ingest job.",
    "dead_priority":
        "Deadline priority of the Ayon ingest job, usually 0-100.",
    "dead_limits":
        "Deadline limits of the Ayon ingest job, comma separated.",
    "dead_limits_2":
        "Deadline job comment of the Ayon ingest job. Empty: not set.",
    "dead_department":
        "Deadline department of the Ayon ingest job.",
    "dead_go_ayon":
        "Also publish the Submission CSV to Ayon on this machine when Go\n"
        "is pressed, like Publish Ayon Local. Needs Project, Folder, Task\n"
        "and Exports > Submission > CSV on.",
    "dead_ayon_folder":
        "Ayon folder path for the CSV ingest, e.g. /shots/sq01/sh010.\n"
        "Required for publishing. No tokens.",
    "dead_ayon_task":
        "Ayon task name for the CSV ingest. Required for publishing.",
    "dead_ayon_product":
        "Ayon product name." + NOT_IMPLEMENTED,
    "dead_ayon_version":
        "Ayon version." + NOT_IMPLEMENTED,
    "dead_ayon_version_check":
        "Check in Ayon whether the version already exists." + NOT_IMPLEMENTED,
    "dead_ayon_version_check_2":
        "Use the next free version when the version exists." + NOT_IMPLEMENTED,

    # ------------------------------------------------------------ Ayon tab
    "ayon_do_shotlist":
        "Read the shot list from Ayon when the package is loaded or reloaded.\n"
        "Needs Project. Server and API key come from install.json.\n"
        "Scan and Export Shot List also work when this is off.",
    "ayon_project":
        "Ayon project name, exact.\n"
        "Used for the shot list and by the Publish Ayon buttons.",
    "ayon_export_csv":
        "Write the shot list as ayon-list.csv to the Output folder\n"
        "(Export Shot List). With Export CSV and Export Excel both off,\n"
        "the CSV is written anyway.",
    "ayon_export_excel":
        "Write the shot list as ayon-list.xlsx to the Output folder\n"
        "(Export Shot List).",
    "ayon_thumbnails":
        "Download folder and task thumbnails to Output/_thumbsDownload\n"
        "when the shot list is read. Needs Output.",
    "ayon_prefix":
        "Prefix of the tokens copied from the matched shot list row.\n"
        "list_ gives {list_Folder Name}, {list_Range}, {list_Task Status},\n"
        "and with Match version {list_Matched Version}...",
    "ayon_path_browse_2":
        "Pick the Output folder.",
    "ayon_filter_assets":
        "Show asset folders in the shot list.",
    "ayon_filter_shots":
        "Show shot folders in the shot list.",
    "ayon_filter_tasks":
        "Show task rows (one row per task of each folder).\n"
        "Task rows are shown for every folder type; Assets / Shots / Other\n"
        "only pick the folder rows.",
    "ayon_filter_other":
        "Show folders that are neither assets nor shots.",
    "ayon_filter_matched":
        "Show only shot list rows matched to package files.\n"
        "Also limits ayon-list.csv and the Matched Versions tab.\n"
        "Shows nothing when no package is loaded.",
    "ayon_filter_tasktype_chbx":
        "Show only tasks of the task types in the next field.",
    "ayon_filter_tasktypes":
        "Task types to show, comma separated, e.g. Compositing, Roto\n"
        "Exact names, not case-sensitive. Needs Tasks on.",
    "ayon_filter_assignee_chbx":
        "Show only tasks assigned to the users in the next field.\n"
        "Only narrows the other filters. Folder rows have no assignees,\n"
        "so they are hidden too.",
    "ayon_filter_assignees":
        "Ayon user names, comma separated, exact, not case-sensitive.\n"
        "A task passes when any of its assignees is listed.",
    "ayon_export_butt":
        "Write ayon-list.csv (and ayon-list-versions.csv with Versions CSV)\n"
        "to Output, with the rows the tables show. Reads Ayon first (like Scan)\n"
        "only when no list is loaded yet. Needs Project and Output;\n"
        "works without Enable and without a loaded package.",
    "ayon_export_go":
        "Also export the shot list (like Export Shot List) when Go is pressed.",
    "ayon_table":
        "Ayon shot list after the filters.\n"
        "Green: the row is matched to a package file.",

    # ------------------------------------------------------------ Preferences tab
    "prefs_frame_rate_txt":
        "Frame rate used for {meta_fps} when metadata fps is not used.\n"
        "Examples: 24, 25, 23.976, 24000/1001. Press Reload to apply.",
    "prefs_frame_rate_use_meta":
        "Use the fps from the file metadata when the file has one.\n"
        "Off: use Frame Rate for all files. Press Reload to apply.",
    "prefs_tc_from_meta":
        "{meta_time_code} is the timecode from the file metadata;\n"
        "for a sequence without one, the frame counter timecode.",
    "prefs_tc_from_counter":
        "{meta_time_code} of a sequence is computed from its frame number\n"
        "and fps; files without a frame number use the metadata timecode.",
    "prefs_tc_default":
        "Timecode for videos and sequences that have none, e.g. 01:00:00:00.\n"
        "Empty: no timecode. Stills never get one. Press Reload to apply.",
    "prefs_size_scan":
        "Read file sizes ({size_bytes}, {size_human}) and check sequences\n"
        "for empty, missing and inconsistent frames.",
    "prefs_size_ignore_first":
        "First frames of each sequence left out of the size check,\n"
        "e.g. 1 for a slate.",
    "prefs_size_neighborhood":
        "Frames on each side whose average size each frame is compared to.",
    "prefs_size_threshold":
        "Warn when a frame's size differs from its neighbours' average\n"
        "by more than this percentage.",
    "prefs_oiio_custom_ocio":
        "Use the OCIO config in the next field as {ocio} in Convert commands,\n"
        "instead of the OCIO environment variable / install.json.\n"
        "Press Reload to apply.",
    "prefs_oiio_custom_ocio_path":
        "Path to an OCIO config file, used when Custom OCIO is on.",
    "prefs_counter_start":
        "First value of the counters {cnt_sub}, {cnt_log} and {cnt_txt}.\n"
        "Each table counts its own visible rows.",
    "prefs_counter_step":
        "Counter increment, e.g. 10 gives 010, 020, 030.",
    "prefs_counter_zeroes":
        "Digits of the counters, e.g. 3 gives 001.",

    # ------------------------------------------------------------ Exports tab
    "text_txt":
        "Write the Text tab content to {package_name}.txt when Go is pressed.",
    "text_root":
        "Save the text file inside the package folder.",
    "text_above":
        "Save the text file next to the package folder (in its parent).",
    "text_custom":
        "Save the text file to the Custom Location folder.",
    "text_custom_path":
        "Existing folder for the text file (Custom Location).",
    "text_add_titles":
        "Add a line with the Text column titles above the rows.",
    "text_sep_tab":
        "Separate the Text columns with a tab.",
    "text_sep_fixed":
        "Separate the Text columns with one space.",
    "text_header":
        "Text above the rows. Package tokens work, e.g. {package_name},\n"
        "{total_txt}, {files_txt}, {total_size_txt_human}, {dd}.{mm}.{yy}\n"
        "Write {{ and }} for literal braces.",
    "text_footer":
        "Text below the rows. Package tokens work, e.g. {total_txt}.\n"
        "Write {{ and }} for literal braces.",

    # ------------------------------------------------------------ Presets tab
    "load_preset_combobox":
        "Saved presets. last_<user> is your state when the app was last closed.",
    "load_preset_button":
        "Load the selected preset into the GUI.\n"
        "Package Folder and Vendor CSV are kept; a loaded package is\n"
        "read again with the new preset.",
    "save_preset_name":
        "Name of the preset to save, without .json.",
    "save_preset_button":
        "Save all settings under the name on the left.\n"
        "A preset with the same name is overwritten without asking.",
    "preset_explore":
        "Open the folder where presets are saved.",
    "preset_mod_text": "Show the bottom Text preview tab.\n"
                       "Hiding a tab does not switch its features off.",
    "preset_mod_sidecar": "Show the Sidecar Files tabs (top and bottom).\n"
                          "Hiding a tab does not switch its features off.",
    "preset_mod_rename": "Show the Rename tabs (top and bottom).\n"
                         "Hiding a tab does not switch its features off.",

    # ------------------------------------------------------------ bottom tabs
    "sub_table":
        "Submission preview. Red: {error}, orange: {warning} (incl. size\n"
        "problems). Edits made here are not exported.\n"
        "Column widths are used for the Excel export.",
    "log_table":
        "Drive Log preview. Edits made here are not exported.\n"
        "Column widths are used for the Excel export.",
    "txt_table":
        "Text export preview. Edits made here are not exported.",
    "side_table":
        "Sidecar files to copy: match result, destination, source.",
    "rename_table":
        "Planned renames: source and destination\n"
        "(paths without extension and frame number).",
    "rename_tab_relative":
        "Show the paths relative to the package folder.",
    "rename_tab_absolute":
        "Show full paths.",
    "rename_tab_names_only":
        "Show file names only.",
    "tree_filter_file":
        "Show only files whose label (number: folder/file name) contains\n"
        "this text. Case-sensitive.",
    "tree_filter_key":
        "Show only tokens whose name contains this text. Case-sensitive.",
    "tree_filter_value":
        "Show only tokens whose value contains this text. Case-sensitive.",
    "data_tree":
        "All tokens of every file, with their values.\n"
        "Use the names as {token} in templates, columns and checks.",
    "file_table":
        "Files found in the package, with size, category and missing frames.\n"
        "Updated on load / Reload.",
}

# Exports tab: the Submission and Drive Log groups share their texts
_EXPORT = {
    "excel": "Write the {what} as .xlsx when Go is pressed.\n"
             "Column widths follow the table on screen.",
    "csv": "Write the {what} as .csv (UTF-8) when Go is pressed.",
    "root": "Save the {what} inside the package folder.",
    "above": "Save the {what} next to the package folder (in its parent).",
    "custom": "Save the {what} to the Custom Location folder.",
    "custom_path": "Existing folder for the {what} (Custom Location).",
    "skip_on": "Don't export rows that have any text in the column\n"
               "named in the next field.",
    "skip": "Column title, exactly as written on the Spreadsheet tab.",
    "split_on": "Write one file per value of the column named in the next\n"
                "field. Files are numbered 001, 002... (see Split Number).",
    "split": "Column title, exactly as written on the Spreadsheet tab.",
    "name": "File name without extension. No tokens.\n"
            "Empty: the package name.",
    "custom_suffix": "Text added after the file name, e.g. _client.",
    "splitnum": "Digits of the split file number, e.g. 3 gives 001.",
}
for _prefix, _what in (("export_sub_", "Submission"), ("export_log_", "Drive Log")):
    for _key, _text in _EXPORT.items():
        TOOLTIPS[_prefix + _key] = _text.format(what=_what)
TOOLTIPS["export_sub_csv"] += "\nRequired by the Publish Ayon buttons."
TOOLTIPS["export_log_name"] += ("\nWith Name and Suffix empty, _log is added when the Submission\n"
                                "is exported too.")

for _what in ("log", "txt"):
    TOOLTIPS[f"{_what}_exclude"] = TOOLTIPS["sub_exclude"]
    TOOLTIPS[f"{_what}_include"] = TOOLTIPS["sub_include"]

_TAB_NAMES = ("package", "parsing", "sidecar", "rename", "data", "ftrack",
              "vendor", "replace", "convert", "spreadsheet", "checks",
              "publish", "ayon", "preferences", "exports", "log", "help",
              "submission", "drivelog", "inspector", "files")
for _tab in _TAB_NAMES:
    TOOLTIPS.setdefault(f"preset_mod_{_tab}", _SHOW_TAB)

for _n in (1, 2, 3):
    TOOLTIPS[f"data_package{_n}_chbx"] = (
        "Use this condition to pair Data CSV rows with files.\n"
        "All conditions that are on must match.")
    TOOLTIPS[f"data_package{_n}"] = (
        "File side of the condition: text with file tokens,\n"
        "e.g. {shot} or {shot}_{task}.\n"
        "Must equal the Data value exactly (case-sensitive).")
    TOOLTIPS[f"data_data{_n}"] = (
        "CSV side of the condition: text with the prefixed column tokens,\n"
        "e.g. {data_shot}. Must equal the Package value exactly.")
    TOOLTIPS[f"ayon_package{_n}_chbx"] = (
        "Use this condition to match shot list rows with files.\n"
        "All conditions that are on must match.")
    TOOLTIPS[f"ayon_package{_n}"] = (
        "File side of the condition: text with file tokens, e.g. {shot}.\n"
        "Must equal the Data value exactly (case-sensitive).")
    TOOLTIPS[f"ayon_list{_n}"] = (
        "Shot list side of the condition: shot list columns in braces,\n"
        "e.g. {Folder Name}, {Folder Path}, {Task Name}, {Task Type}.")


# Numbered rows: (regex on objectName, tooltip)
ROW_TOOLTIPS = [
    # Parsing
    (r"parse_name_\d+$",
     "Name of the token this row creates, used as {name} elsewhere.\n"
     "Rows run top to bottom; lower rows can use tokens of upper rows.\n"
     "A lower row with the same name overwrites the value.\n"
     "The row is skipped when Name, Pattern or Source is empty."),
    (r"parse_pattern_\d+$",
     "Regex run on Source. Case-sensitive.\n"
     "Repl empty: the token is capture group 1, or the whole match\n"
     "when the pattern has no group (empty if no match).\n"
     "Repl set: every match in Source is replaced; a Source that\n"
     "doesn't match is used unchanged, so anchor with ^ and $.\n"
     "Example: ^([^_]+_[^_]+)_"),
    (r"parse_repl_\d+$",
     "Replacement, e.g. \\1_\\2. Empty: use capture group 1 (whole match without a group).\n"
     "Starting with lambda runs Python on the match:\n"
     "lambda m: m.group(1).upper()"),
    (r"parse_source_\d+$",
     "Text the Pattern is run on, with tokens.\n"
     "{name} = file name without extension, {part1} = file name,\n"
     "{part2} = parent folder, {part3} = folder above...\n"
     "If a token is unknown, the result is empty."),
    (r"parse_filter_\d+$",
     "Run this row only for files whose full path contains this text.\n"
     "Plain text, case-sensitive. Empty: all files. Example: .exr"),
    # Sidecar
    (r"side_pattern_\d+$",
     "Regex run on the sidecar file name (no folder).\n"
     "Repl empty: the result is capture group 1, or the whole match\n"
     "without a group (no match: file ignored).\n"
     "Example: ^(\\w+_\\d+)\\.cdl$"),
    (r"side_repl_\d+$",
     "Optional replacement for the file name, e.g. \\1_\\2.\n"
     "Starting with lambda runs Python. Empty: use capture group 1."),
    (r"side_match_\d+$",
     "Package file tokens the result must equal, e.g. {shot}.\n"
     "Exact, case-sensitive. The sidecar is linked to every equal file."),
    (r"side_dest_\d+$",
     "Copy destination with tokens. Include the file name, e.g.\n"
     "{package_name_root}/{package_name}/cdl/{sidecar_file}\n"
     "Sidecar tokens: {sidecar_path} {sidecar_file} {sidecar_ext}\n"
     "{sidecar_result}. File tokens like {shot} work too."),
    (r"side_filter_\d+$",
     "Use this row only for sidecar files whose name contains this text.\n"
     "Plain text, case-sensitive. Empty: all sidecar files. Example: .cdl"),
    # Rename
    (r"rename_filter_\d+$",
     "Python condition; the row applies only to files where it is True.\n"
     "Tokens are pasted in as text, so quote them:\n"
     "'{extension}' == 'exr'\n"
     "Empty: all files."),
    (r"rename_source_\d+$",
     "Part of the path to rename:\n"
     "0 = whole path, 1 = file name, 2 = parent folder,\n"
     "3 = the folder above, ...\n"
     "Extension and frame number are never renamed."),
    (r"rename_pattern_\d+$",
     "Regex to find in the chosen part. Tokens allowed.\n"
     "Rows run in order; each works on the result of the previous one.\n"
     "Regex counts like \\d{3} work. A row with an unknown {token}\n"
     "is skipped.\n"
     "Example: ^0x0$"),
    (r"rename_repl_\d+$",
     "Replacement with tokens, e.g. {width}x{height}.\n"
     "Starting with lambda runs Python. The row is off when empty.\n"
     "A row with an unknown {token} or other braces is skipped."),
    # Convert
    (r"thumbs_if_\d+$",
     "Python condition; the command runs only for files where it is True.\n"
     "Tokens are pasted in as text, so quote them:\n"
     "'{extension}' in ['exr', 'dpx']\n"
     "Empty: all files."),
    (r"thumbs_exe_\d+$",
     "Program to run. {ffmpeg} {ffprobe} {oiio} {vfx-transcode} are the\n"
     "tools SH found (PATH, environment, install.json); a plain name like\n"
     "ffmpeg is looked up on the system PATH.\n"
     "Paths are not quoted, so avoid spaces."),
    (r"thumbs_args_\d+$",
     "Command line arguments with tokens. Quote paths yourself, e.g.\n"
     "-y -i \"{path}\" -ss {meta_thumbnail_time} -vframes 1 \"<out>.jpg\"\n"
     "{ocio} is the OCIO config. Write the output to the File Name path."),
    (r"thumbs_name_\d+$",
     "Output file the command creates, with tokens. Required.\n"
     "Used by Skip Existing, and as {convert_path01}... and\n"
     "{convert_path_relative01}... in spreadsheets. 01 is the first row\n"
     "with Arguments and File Name filled, 02 the next one, and so on.\n"
     "A name with an unknown {token} skips the command."),
    # Checks
    (r"check_if_\d+$",
     "Optional Python condition; the check runs only where it is True.\n"
     "Tokens are pasted in as text, so quote strings:\n"
     "'{extension}' == 'exr'\n"
     "Empty: all files. An invalid expression counts as False."),
    (r"check_check_\d+$",
     "Python expression; the file is flagged when it is True.\n"
     "Examples: '{meta_fps}' != '24'    {meta_width} != 1920\n"
     "Quote text tokens. An invalid expression counts as False.\n"
     "Empty: this check is off."),
    (r"check_warning_\d+$",
     "Add the message to {warning}; the row turns orange."),
    (r"check_error_\d+$",
     "Add the message to {error}; the row turns red."),
    (r"check_message_\d+$",
     "Message added when the check fires. Tokens allowed.\n"
     "Empty: Error check NN / Warning check NN."),
]
_ROW_TOOLTIPS = [(re.compile(p), t) for p, t in ROW_TOOLTIPS]


def tooltip_for(name):
    """Tooltip text for a widget objectName, or None."""
    if name in TOOLTIPS:
        return TOOLTIPS[name]
    for pattern, text in _ROW_TOOLTIPS:
        if pattern.match(name):
            return text
    return None


def to_rich_text(text):
    """Plain text -> Qt rich text: wraps long lines, keeps < > literal."""
    return "<qt>" + html.escape(text).replace("\n", "<br>") + "</qt>"


def apply_tooltips(ui):
    """Set the tooltip of every widget of ``ui`` (a Ui_submission) found in
    TOOLTIPS / ROW_TOOLTIPS. Returns the number of tooltips set."""
    count = 0
    for name, widget in vars(ui).items():
        text = tooltip_for(name)
        if text is None or not hasattr(widget, "setToolTip"):
            continue
        widget.setToolTip(to_rich_text(text))
        count += 1
    return count

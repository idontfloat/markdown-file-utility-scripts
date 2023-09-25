# Markdown File Utility Scripts

This repository contains two Python scripts to help manage Markdown files:

1. `rename-md-files.py`: Renames Markdown files based on their H1 title.
2. `insert-h1-from-filename.py`: Inserts an H1 title from the filename if the file is missing an H1 title.

## Requirements

- Python 3.x

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/markdown-file-utility.git
```

Navigate to the directory:

```bash
cd markdown-file-utility
```

## Usage

### Rename Markdown Files Based on H1 Title (`rename-md-files.py`)

This script renames Markdown files in the current directory and its subdirectories based on the H1 title found in each file.

#### Command-Line Options

- `--dry-run`: Perform a dry run without actually renaming files.
- `--exclude-folders`: Comma-separated list of folders to exclude from the operation.

#### Example

```bash
python rename-md-files.py --dry-run --exclude-folders=folder1,folder2
```

### Insert H1 Title from Filename (`insert-h1-from-filename.py`)

This script inserts an H1 title at the beginning of Markdown files that are missing an H1 title. The title is taken from the filename. If frontmatter exists, the title is inserted after it.

#### Command-Line Options

- `--dry-run`: Perform a dry run without actually making changes.
- `--exclude-folders`: Comma-separated list of folders to exclude from the operation.

#### Example

```bash
python insert-h1-from-filename.py --dry-run --exclude-folders=folder1,folder2
```

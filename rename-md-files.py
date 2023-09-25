import os
import re
import argparse

def sanitize_title(title):
    return re.sub(r'[\/:*?"<>|]', '', title)

def get_first_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
        match = re.match(r'^#\s+(.*)', first_line)
        if match:
            return sanitize_title(match.group(1))
    return None

def main(dry_run, exclude_folders):
    exclude_folders = set(exclude_folders.split(',')) if exclude_folders else set()
    for folder_path, _, filenames in os.walk(os.getcwd()):
        if any(exclude in folder_path for exclude in exclude_folders):
            continue
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                title = get_first_h1_title(file_path)
                if title:
                    new_filename = f"{title}.md"
                    if filename == new_filename:
                        print(f"Skipped {file_path} (Already named correctly)")
                        continue
                    new_file_path = os.path.join(folder_path, new_filename)
                    if dry_run:
                        print(f"[Dry Run] Would rename {file_path} to {new_file_path}")
                    else:
                        os.rename(file_path, new_file_path)
                        print(f"Renamed {file_path} to {new_file_path}")
                else:
                    print(f"Skipped {file_path} (No H1 title on the first line)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rename Markdown files based on their H1 title.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without renaming files.')
    parser.add_argument('--exclude-folders', type=str, help='Comma-separated list of folders to exclude.')
    args = parser.parse_args()
    main(dry_run=args.dry_run, exclude_folders=args.exclude_folders)

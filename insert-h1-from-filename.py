import os
import re
import argparse

def has_h1_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if re.match(r'^#\s+', line):
                return True
    return False

def insert_h1_from_filename(file_path, filename):
    title = os.path.splitext(filename)[0]
    with open(file_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        
        frontmatter_end = content.find('---', 3)
        if frontmatter_end != -1:
            frontmatter_end += 3
            f.write(content[:frontmatter_end] + f"\n\n# {title}\n\n" + content[frontmatter_end:])
        else:
            f.write(f"# {title}\n\n{content}")

def main(dry_run, exclude_folders):
    exclude_folders = set(exclude_folders.split(',')) if exclude_folders else set()
    for folder_path, _, filenames in os.walk(os.getcwd()):
        if any(exclude in folder_path for exclude in exclude_folders):
            continue
        for filename in filenames:
            if filename.endswith('.md'):
                file_path = os.path.join(folder_path, filename)
                if not has_h1_title(file_path):
                    if dry_run:
                        print(f"[Dry Run] Would insert H1 title from filename {file_path}")
                    else:
                        insert_h1_from_filename(file_path, filename)
                        print(f"Inserted H1 title from filename {file_path}")
                else:
                    print(f"Skipped {file_path} (Already has H1 title)")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Insert H1 title from filename if missing.')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes.')
    parser.add_argument('--exclude-folders', type=str, help='Comma-separated list of folders to exclude.')
    args = parser.parse_args()
    main(dry_run=args.dry_run, exclude_folders=args.exclude_folders)

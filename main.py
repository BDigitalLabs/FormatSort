import sys
from pathlib import Path
import shutil
import argparse

parser = argparse.ArgumentParser(
    description="FormatSort - File Organizer"
)

parser.add_argument(
    "directory",
    nargs="?",
    type=Path,
    default=Path("."),
    help="Target directory"
)

parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Preview operations without modifying files"
)

parser.add_argument(
    "--move",
    action="store_true",
    help="Move files instead of copying them"
)

parser.add_argument(
    "--version",
    action="version",
    version="FormatSort v1.0.0"
)

args = parser.parse_args()

directory = args.directory.expanduser()

if not directory.is_dir():
    parser.error(f"Invalid directory: {directory}")

move_status = args.move





document_formats = (
    ".doc",
    ".docx",
    ".odt",
    ".pdf",
    ".txt",
    ".rtf",
    ".md",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".csv",
    ".odp",
    ".ods"
)


picture_formats = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".svg",
    ".tiff",
    ".tif",
    ".heic",
    ".heif",
    ".ico",
    ".avif"
)

video_formats = (".mp4",".mkv",".avi",".mov",".wmv",".webm",".flv",".mpeg", ".mpg")

music_formats = (".mp3",".wav",".flac",".aac",".ogg",".opus",".m4a",".wma",".mid", ".midi")

archive_formats = (".zip",".rar",".7z",".tar",".gz",".bz2",".xz",".zst")

program_formats = (".exe",".msi",".deb",".rpm",".AppImage",".apk",".dmg")

development_formats = (
    ".py",
    ".cs",
    ".java",
    ".js",
    ".ts",
    ".html",
    ".css",
    ".cpp",
    ".hpp",
    ".c",
    ".h",
    ".go",
    ".rs",
    ".php",
    ".json",
    ".xml",
    ".yaml",
    ".yml"
)

ebook_formats = [
    ".epub",
    ".mobi",
    ".azw",
    ".azw3",
    ".djvu"
]

font_formats = [
    ".ttf",
    ".otf",
    ".woff",
    ".woff2",
    ".eot"
]

design_formats = [
    ".psd",
    ".psb",
    ".ai",
    ".eps",
    ".indd",
    ".xcf",
    ".sketch",
    ".fig"
]

model_3d_formats = [
    ".blend",
    ".obj",
    ".stl",
    ".fbx",
    ".gltf",
    ".glb",
    ".dae",
    ".3ds",
    ".step",
    ".stp"
]

database_formats = [
    ".db",
    ".sqlite",
    ".sqlite3",
    ".mdb",
    ".accdb",
    ".sql"
]

backup_formats = [
    ".bak",
    ".backup",
    ".old",
    ".orig",
    ".dump"
]

log_formats = [
    ".log",
    ".logs",
    ".trace"
]

format_categories = {
    "Documents": document_formats,
    "Pictures": picture_formats,
    "Videos": video_formats,
    "Music": music_formats,
    "Archives": archive_formats,
    "Programs": program_formats,
    "Development": development_formats,
    "Ebooks": ebook_formats,
    "Fonts": font_formats,
    "Design": design_formats,
    "3D": model_3d_formats,
    "Databases": database_formats,
    "Backups": backup_formats,
    "Logs": log_formats
}

extension_categories = {
    extension.lower(): category
    for category, extensions in format_categories.items()
    for extension in extensions
}




def print_files(directory):
    print("========== Files ==========")
    for file in directory.iterdir():
        if file.is_file():
            print(file.name)
    print("===========================")


def organize_files(directory, move=False,dry_run=False):

    files = [
        file for file in directory.iterdir()
        if file.is_file()
    ]



    for file in files:
        category = extension_categories.get(
            file.suffix.lower(),
            "Other"
        )

        extension = file.suffix[1:].upper() or "No Extension"

        new_directory = directory / category / extension

            

        destination = new_directory / file.name

        if destination.exists():
            print(f"Skipped: {file.name} (Already exists)")
            continue

        if dry_run:
            operation = "Move" if move else "Copy"
            print(f"[DRY RUN] {operation}: {file.name} -> {destination}")
            continue

            

        try:
            new_directory.mkdir(
                parents=True,
                exist_ok=True
            )
            if move:
                shutil.move(file, destination)
                print(f"Moved: {file.name}")
            else:
                shutil.copy2(file, destination)
                print(f"Copied: {file.name}")

        except OSError as error:
            print(f"Error: {file.name} | {error}")


print_files(directory)
user_input = input("Do you want to continue? [Y/N]: ").strip().upper()

if user_input == "N":
    sys.exit()
elif user_input != "Y":
    print("Invalid value | Y = Yes - N = No")
    sys.exit()

organize_files(
    directory,
    move=move_status,
    dry_run=args.dry_run
)
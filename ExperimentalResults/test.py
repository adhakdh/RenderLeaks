from pathlib import Path

IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".idea",
    ".vscode",
}

IGNORE_FILES = {
    ".DS_Store",
}

def print_tree(path: Path, prefix: str = ""):
    items = sorted(
        [p for p in path.iterdir()
         if p.name not in IGNORE_DIRS and p.name not in IGNORE_FILES],
        key=lambda p: (p.is_file(), p.name.lower())
    )

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "
        print(prefix + connector + item.name + ("/" if item.is_dir() else ""))

        if item.is_dir():
            extension = "    " if is_last else "│   "
            print_tree(item, prefix + extension)

if __name__ == "__main__":
    print(".")
    print_tree(Path("."))
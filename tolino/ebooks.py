import epub_meta
from pathlib import Path

def get_epubs(epubs_path):
    epubs = list(Path(epubs_path).rglob("*.epub"))
    epubs.sort(key=lambda file: file.lstat().st_mtime, reverse=True)

    return epubs

def read_info(epub_path):
    full_path = epub_path.resolve()

    try:
        return epub_meta.get_epub_metadata(full_path)
    except:
        return None
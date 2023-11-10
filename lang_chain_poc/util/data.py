from pathlib import Path


def data_file_path(file_name: str) -> str:
    return str(Path(__file__).parent.parent.parent / f'data/{file_name}')

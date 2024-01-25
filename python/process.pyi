# generated with `stubgen process.py`

import logging

LOGGER: logging.Logger

def get_entries(inpath: str) -> int: ...
def get_process_info(process: str, prod_tag: str, input_dir: str) -> tuple[list[str], list[int]]: ...
def get_process_info_files(process: str, input_dir: str) -> tuple[list[str], list[int]]: ...
def get_process_info_yaml(process: str, prod_tag: str) -> tuple[list[str], list[int]]: ...
def get_process_dict(proc_dict_location: str) -> dict: ...
def get_process_dict_dirs() -> list[str]: ...
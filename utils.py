import aiofiles.os
import hashlib
import os

import const


async def get_or_create_dir(filename):
    directory = f'{const.STORAGE_FOLDER}{filename[:2]}'
    if not os.path.exists(directory):
        await aiofiles.os.mkdir(directory)
    return directory


def get_files(folder):
    file_list = []
    for _, __, files in os.walk(folder, topdown=False):
        file_list.extend(filter(lambda x: not x.startswith('.'), files))
    return file_list


async def get_file_path(filename):
    directory = await get_or_create_dir(filename)
    return f'{directory}/{filename}'


def is_exist(path):
    return os.path.isfile(path)


async def save_file(filename, file):
    file.seek(0)
    path = await get_file_path(filename)
    async with aiofiles.open(path, 'wb') as f:
        await f.write(file.read())
    return filename


def get_hash(file, blocksize=65536):
    hasher = hashlib.md5()
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    file.seek(0)
    return hasher.hexdigest()


async def delete_file(filename):
    path = await get_file_path(filename)
    try:
        await aiofiles.os.remove(path)
        return True
    except FileNotFoundError:
        return False

import os

import pytest

from downloader import Downloader

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def downloaded_path() -> str:
    return '/Users/dzmitry/Projects/download-master/tests/downloaded'


@pytest.fixture(autouse=True)
def remove_created_files(downloaded_path: str) -> None:
    yield
    for x in os.listdir(downloaded_path):
        os.remove(f'{downloaded_path}/{x}')


@pytest.fixture
def downloader(downloaded_path: str) -> Downloader:
    return Downloader(
        download_path=downloaded_path,
        links_path='/Users/dzmitry/Projects/download-master/tests/links.txt',
        simultaneous_tasks=1,
        timeout=1,
    )

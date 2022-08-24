from asyncio import Semaphore
from os import path

import pytest
from aiohttp import ClientSession

from downloader import Downloader


@pytest.mark.asyncio
async def test_download__incorrect_url(downloader: Downloader, capfd) -> None:
    url = 'incorrect_url'
    semaphore = Semaphore(downloader.simultaneous_tasks)

    await downloader._download(url, ClientSession(), semaphore)

    out, _ = capfd.readouterr()
    assert f'Failed to download url {url}: <InvalidURL {url}>' in out


@pytest.mark.asyncio
async def test_download__non_200(downloader: Downloader, capfd) -> None:
    url = 'https://cdn-9.motorsport.com/images/mgl/24vA3r46/s500/max-verstappen-red-bull-racing.webp'
    semaphore = Semaphore(downloader.simultaneous_tasks)

    await downloader._download(url, ClientSession(), semaphore)

    out, _ = capfd.readouterr()
    assert f'Failed to download url {url}. Status: 403' in out


@pytest.mark.asyncio
async def test_download(downloader: Downloader, capfd) -> None:
    url = 'https://cdn-9.motorsport.com/images/mgl/24vA3r46/s500/max-verstappen-red-bull-racing-1.webp'
    semaphore = Semaphore(downloader.simultaneous_tasks)

    await downloader._download(url, ClientSession(), semaphore)

    assert path.exists(f'{downloader.download_path}/max-verstappen-red-bull-racing-1.webp')

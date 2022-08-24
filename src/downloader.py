import os
from asyncio import Semaphore, gather, wait_for
from urllib.parse import urlparse

import aiofiles
from aiohttp import ClientSession


class Downloader:
    def __init__(self, download_path, links_path, simultaneous_tasks, timeout) -> None:
        self.download_path = download_path
        self.links_path = links_path
        self.simultaneous_tasks = simultaneous_tasks
        self.timeout = timeout

    async def _download(self, url, session, semaphore):
        async with semaphore:
            print(f'Downloading: {url}')
            try:
                async with session.get(url) as r:
                    content = await r.read()
            except Exception as e:
                print(f'Failed to download url {url}: {e.__repr__()}')
                return

            if r.status != 200:
                print(f'Failed to download url {url}. Status: {r.status}')
                return
            url_obj = urlparse(url)
            async with aiofiles.open(f'{self.download_path}/{os.path.basename(url_obj.path)}', '+wb') as f:
                await f.write(content)

    async def run(self):
        tasks = []
        semaphore = Semaphore(self.simultaneous_tasks)

        async with ClientSession() as session:
            async with aiofiles.open(self.links_path) as f:
                async for url in f:
                    tasks.append(
                        wait_for(
                            self._download(url.rstrip(), session, semaphore),
                            timeout=self.timeout,
                        )
                    )
                return await gather(*tasks)

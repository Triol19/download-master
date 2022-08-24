import argparse
from asyncio import run
from os import path

from downloader import Downloader
from src.exceptions import DownloadPathDoesNotExist, LinksPathDoesNotExist

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download-Master')
    parser.add_argument(
        '-dp', '--download-path', help='Downloading path', default='/Users/dzmitry/Downloads'
    )
    parser.add_argument(
        '-lp', '--links-path', help='Path to the file with links'
    )
    parser.add_argument(
        '-st', '--simultaneous-tasks', help='Max number of simultaneous tasks', type=int, default=10
    )
    parser.add_argument(
        '-t', '--timeout', help='Timeout for one task (in seconds)', type=int, default=3
    )

    args = parser.parse_args()
    if not path.isdir(args.download_path):
        raise DownloadPathDoesNotExist(args.download_path)
    if not path.exists(args.links_path):
        raise LinksPathDoesNotExist(args.links_path)

    d = Downloader(args.download_path, args.links_path, args.simultaneous_tasks, args.timeout)
    run(d.run())

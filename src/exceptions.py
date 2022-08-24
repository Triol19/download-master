class DownloaderBaseException(Exception):
    pass


class ArgumentException(DownloaderBaseException):
    pass


class DownloadPathDoesNotExist(ArgumentException):
    pass


class LinksPathDoesNotExist(ArgumentException):
    pass

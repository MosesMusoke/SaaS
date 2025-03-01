from .downloader import download_to_local

__all__ = ['download_to_local']

# By using this "__all__ = ['download_to_local']" python ensures that only download_to_local is accessible when someone does "from myapp import *"
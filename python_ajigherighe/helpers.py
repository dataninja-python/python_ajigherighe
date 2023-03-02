
# define a general exception when an import error occurs
class InvalidImportException(Exception):
    """Raised when a required module or package is not imported"""
    pass


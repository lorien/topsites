MONGODB = {
    'connection': {},
    'dbname': 'topsites',
}

try:
    from project.settings_local import *
except ImportError:
    pass

import os
import glob
from zipfile import ZipFile

from ioweb.stat import Stat


BATCHES = {
    'top1k': {
        'number': 1000,
    },
}


def setup_arg_parser(parser):
    parser.add_argument('batch')


def main(batch, **kwargs):
    stat = Stat(speed_keys=['file'])
    config = BATCHES[batch]
    files = sorted(glob.glob('data/html/%s/*.html' % batch))
    step = 100
    print('Clearing zip dir')
    for path in glob.glob('data/zip/%s/*.zip' % batch):
        print('Removing %s' % path)
        os.unlink(path)
    print('Creating zip files')

    batch_dir = 'data/zip/%s' % batch
    if not os.path.exists(batch_dir):
        os.makedirs(batch_dir)
    for idx in range(0, config['number'], step):
        zpath = 'data/zip/%s/%03d.zip' % (batch, idx)
        print('Writing to %s' % zpath)
        stat.inc('zip-file')
        with ZipFile(zpath, 'w') as zfile:
            for path in files[idx:idx + step]:
                stat.inc('html-file')
                fname = os.path.split(path)[1]
                zfile.write(path, fname)

# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from os.path import join
from logging import getLogger

from skbio.io import read


logger = getLogger(__name__)


def parse(out_dir, fn='minced.gff'):
    '''Parse the annotation and add it to interval metadata.

    Parameters
    ----------
    out_dir : str
        the output dir
    seq_fn : str
        input seq file name. With `out_dir` and `seq_fn`, you should
        be able to create the file name outputted from this prediction
        tool.

    '''
    logger.debug('Parsing minced prediction')
    fp = join(out_dir, 'minced.gff')
    return read(fp, format='gff3')

# ----------------------------------------------------------------------------
# Copyright (c) 2015--, micronota development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from os.path import join
from logging import getLogger

import click

from ..database.rfam import filter_models


logger = getLogger(__name__)


# keep this command hidden from help msg
@click.command(hidden=True)
@click.option('--operation', type=click.Choice(['kingdom', 'other', 'all']),
              default='kingdom', required=True, help='')
@click.argument('infile', type=click.File('r'), nargs=1)
@click.argument('outfile', type=click.Path(),  nargs=1)
@click.pass_context
def cli(ctx, operation, infile, outfile):
    '''Create rfam database for micronota usage.'''
    if operation in ['other', 'all']:
        with open(join(outfile, 'miscRfam.cm'), 'w') as outfile:
            filter_models(infile, outfile)
    if operation in ['kingdom', 'all']:
        kingdom_models = {'bacteria': {('RF00001', '5S_rRNA'),
                                       ('RF00177', 'SSU_rRNA_bacteria'),
                                       ('RF02541', 'LSU_rRNA_bacteria')},
                          'archaea': {('RF00001', '5S_rRNA'),
                                      ('RF01959', 'SSU_rRNA_archaea'),
                                      ('RF02540', 'LSU_rRNA_archaea')},
                          'eukarya': {('RF00001', '5S_rRNA'),
                                      ('RF00002', '5_8S_rRNA'),
                                      ('RF01960', 'SSU_rRNA_eukarya'),
                                      ('RF02543', 'LSU_rRNA_eukarya')}}
        for kingdom in kingdom_models:
            with open(join(outfile, kingdom + '.cm'), 'w') as outfile:
                filter_models(infile, outfile, negate=True, models=kingdom_models[kingdom])
            # don't forget to restart from the beginning of the file.
            infile.seek(0, 0)
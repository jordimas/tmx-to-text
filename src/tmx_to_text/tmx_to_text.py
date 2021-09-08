#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import datetime
import resource
from optparse import OptionParser
from .converttmx import ConvertTmx


def read_parameters():
    parser = OptionParser()

    parser.add_option(
        '-f',
        '--tmx-file',
        type='string',
        action='store',
        dest='tmx_file',
        help='tmx File to convert to Text'
    )

    parser.add_option(
        '-s',
        '--source_lang',
        type='string',
        action='store',
        default='en',
        dest='source_language',
        help='Source language to export'
    )

    parser.add_option(
        '-t',
        '--target_lang',
        type='string',
        action='store',
        dest='target_language',
        help='Target language to export'
    )

    parser.add_option(
        '-p',
        '--prefix',
        type='string',
        action='store',
        dest='prefix',
        default='',
        help='Filename prefix used in the generated text files'
    )

    parser.add_option(
        '-d',
        '--debug',
        action='store_true',
        dest='debug',
        default=False,
        help=u'Debug memory and execution time'
    )

    (options, args) = parser.parse_args()
    if options.tmx_file is None:
        parser.error('TMX file not given')

    if options.target_language is None:
        parser.error('target_language file not given')

    return options.tmx_file, options.source_language, options.target_language, options.prefix, options.debug



def main():

    print("Converts TMX into two text files.")
    print("Use -h for more information.")

    tmx_file, source, target, prefix, debug = read_parameters()

    if len(prefix) > 0:
        prefix = prefix + "."

    txt_en_file = f'{prefix}{source}-{target}.{source}'
    txt_ca_file = f'{prefix}{source}-{target}.{target}'

    if debug:
        start_time = datetime.datetime.now()

    convert = ConvertTmx(tmx_file, txt_en_file, txt_ca_file)
    convert.convert(source, target)

    if debug:
        max_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024 
        print(f"max_rss {max_rss} MB")

        s = 'Execution time: {0}'.format(datetime.datetime.now() - start_time)
        print(s)

if __name__ == "__main__":
    main()

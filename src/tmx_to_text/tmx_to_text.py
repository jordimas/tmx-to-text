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
from .converttmx import ConvertTmx
from .infotmx import InfoTmx
import argparse

def read_parameters():

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')
    info = subparser.add_parser('info')
    info.add_argument('-f', type=str, dest='tmx_file', required=True, help= "TMX file to show info")

    convert = subparser.add_parser('convert')
    convert.add_argument('-f', type=str, dest='tmx_file', required=True, help= "TMX file to convert")
    convert.add_argument('-s', '--source_lang', type=str, required=True, dest='source_lang', help="Source language to export")
    convert.add_argument('-t', '--target_lang', type=str, required=True, dest='target_lang', help="Target language to export")
    convert.add_argument('-p', '--prefix', type=str, dest='prefix', default='', help="Filename prefix used in the generated text files")
    convert.add_argument('-d', '--debug', action='store_true', default=False, dest='debug', help="Debug memory and execution time")
    args = parser.parse_args()
    return args

def convert(args):
    tmx_file = args.tmx_file
    source = args.source_lang
    target = args.target_lang
    prefix = args.prefix
    debug = args.debug

    if prefix:
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

def info(args):
    tmx_file = args.tmx_file

    info = InfoTmx(args.tmx_file)
    languages = info.get_information()
    for language in languages.keys():
        sentences = languages[language]
        print(f"language '{language}' - sentences: {sentences}")

def main():

    print("Converts TMX into two text files and shows info.")
    print("Use -h for more information.")

    args = read_parameters()
    if args.command == "convert":
        convert(args)
    elif args.command == "info":
        info(args)

if __name__ == "__main__":
    main()

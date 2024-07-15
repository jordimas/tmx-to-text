#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Jordi Mas i Hernandez <jmas@softcatala.org>
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

import lxml.etree


class ConvertTmx():

    def __init__(self, input_file, en_filename, ca_filename):
        self.input_file = input_file
        self.en_filename = en_filename
        self.ca_filename = ca_filename

    def convert(self, source_language, target_language, nodup_source = False, nodup_target = False):
        entries = 0
        duplicated_source = 0
        duplicated_target = 0
        seen_sources = set()
        seen_targets = set()
        tf_en = open(self.en_filename, 'w')
        tf_ca = open(self.ca_filename, 'w')

        fp = open(self.input_file, 'rb')
        context = lxml.etree.iterparse(fp, events=['start', 'end'], recover=True)

        tu = {}
        lang = ""
        for action, elem in context:

            if elem.tag == "tu" and action == "start":
                tu = {}
                elem.clear()
                continue

            if elem.tag == "tuv" and action == "start":
                if "lang" in elem.attrib: 
                    lang = elem.attrib['lang'].lower()
                elif '{http://www.w3.org/XML/1998/namespace}lang' in elem.attrib:
                    lang = elem.attrib['{http://www.w3.org/XML/1998/namespace}lang'].lower()

                elem.clear()
                continue

            if elem.tag == "seg" and action == "end":
                text = elem.text
                if text is not None:
                    tu[lang] = text
                elem.clear()
                continue

            if elem.tag == "tu" and action == "end":
                if len(tu) == 0:
                    elem.clear()
                    continue

                source = tu.get(source_language)
                translation = tu.get(target_language)
                if not source or not translation:
                    elem.clear()
                    continue

                source = source.replace("\n", '')
                translation = translation.replace("\n", '')

                write_entry = True
                if nodup_source:
                    hash_source = hash(source)
                    if hash_source in seen_sources:
                        write_entry = False
                        duplicated_source += 1
                    else:
                        seen_sources.add(hash_source)

                if nodup_target:
                    hash_target = hash(translation)
                    if hash_target in seen_targets:
                        write_entry = False
                        duplicated_target += 1
                    else:
                        seen_targets.add(hash_target)

                if write_entry:
                    tf_en.write(source + "\n")
                    tf_ca.write(translation + "\n")
                    entries = entries + 1

                tu.clear()
                elem.clear()

        tf_en.close()
        tf_ca.close()
        fp.close()
        print(f"Wrote {entries} strings")
        if nodup_source:
            print(f"Duplicates {duplicated_source} strings in source")
        if nodup_target:
            print(f"Duplicates {duplicated_target} strings in target")
        if entries == 0:
            print(f"Make sure using 'info' command that there are actually strings for both languages '{source_language}' and '{target_language}'")

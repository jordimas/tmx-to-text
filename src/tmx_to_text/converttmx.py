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

    def convert(self, source_language, target_language):
        entries = 0

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
                    continue

                source = source.replace("\n", '')
                translation = translation.replace("\n", '')

                tf_en.write(source + "\n")
                tf_ca.write(translation + "\n")

                entries = entries + 1
                tu.clear()

                elem.clear()


        tf_en.close()
        tf_ca.close()
        fp.close()
        print("Wrote {0} strings".format(entries))

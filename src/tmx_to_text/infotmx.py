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

import lxml.etree


class InfoTmx():

    def __init__(self, input_file):
        self.input_file = input_file

    def get_information(self):

        fp = open(self.input_file, 'rb')
        context = lxml.etree.iterparse(fp, events=['start', 'end'], recover=True)
        
        lang = ""
        lang_sentences = {}

        for action, elem in context:
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
                    if lang in lang_sentences:
                        sentences = lang_sentences[lang] + 1
                        lang_sentences[lang] = sentences
                    else:
                        lang_sentences[lang] = 1

                elem.clear()

        fp.close()
        return lang_sentences


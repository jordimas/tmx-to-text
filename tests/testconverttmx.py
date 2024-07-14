# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Jordi Mas i Hernandez <jmas@softcatala.org>
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

from src.tmx_to_text.converttmx import ConvertTmx
import unittest
from os import path
import tempfile

class TestConvertTmx(unittest.TestCase):

    def _get_tmx_file(self, filename):
        tmx_file = path.dirname(path.realpath(__file__))
        tmx_file += '/data/{0}'.format(filename)
        return tmx_file

    def _get_lines(self, source_file, target_file):
        with open(source_file) as file:
            source_lines = file.readlines()

        with open(target_file) as file:
            target_lines = file.readlines()

        return source_lines, target_lines

    def test_conversion_simple(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('simple.tmx')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(1, len(source_lines))
        self.assertEquals(1, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner"')

    def test_conversion_lang(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('simple-lang.tmx')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(1, len(source_lines))
        self.assertEquals(1, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner"')

    def test_conversion_simple_long_lang(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('error.tmx')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(2, len(source_lines))
        self.assertEquals(2, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), 'And, in the best case, freedom will compensate us.')
        self.assertEquals(target_lines[0].rstrip(), 'I que, en el millor dels casos, ens recompensarà amb llibertat.^C»')

        self.assertEquals(source_lines[1].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[1].rstrip(), 'Alineador de textos "Aligner"')

    def test_conversion_simple_lang_does_exits(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('error.tmx')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("de", "nl")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(0, len(source_lines))
        self.assertEquals(0, len(target_lines))

    def test_conversion_nodup_source_no(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('duplicate_source.xml')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(2, len(source_lines))
        self.assertEquals(2, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner" 1')
        self.assertEquals(source_lines[1].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[1].rstrip(), 'Alineador de textos "Aligner" 2')
        
    def test_conversion_nodup_source_yes(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('duplicate_source.xml')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca", True)

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(1, len(source_lines))
        self.assertEquals(1, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner" 1')

    def test_conversion_nodup_target_no(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('duplicate_target.xml')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca")

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(2, len(source_lines))
        self.assertEquals(2, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility 1')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner"')
        self.assertEquals(source_lines[1].rstrip(), '"Aligner" aligner utility 2')
        self.assertEquals(target_lines[1].rstrip(), 'Alineador de textos "Aligner"')

    def test_conversion_nodup_target_yes(self):
        source_file = tempfile.NamedTemporaryFile().name
        target_file = tempfile.NamedTemporaryFile().name

        tmx_file = self._get_tmx_file('duplicate_target.xml')
        convertTmx = ConvertTmx(tmx_file, source_file, target_file)
        convertTmx.convert("en", "ca", False, True)

        source_lines, target_lines = self._get_lines(source_file, target_file)
        self.assertEquals(1, len(source_lines))
        self.assertEquals(1, len(target_lines))
        self.assertEquals(source_lines[0].rstrip(), '"Aligner" aligner utility 1')
        self.assertEquals(target_lines[0].rstrip(), 'Alineador de textos "Aligner"')
if __name__ == '__main__':
    unittest.main()

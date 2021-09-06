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
import tempfile
from os import path


class TestConvertTmx(unittest.TestCase):

    def _get_tmx_file(self, filename):
        tmx_file = path.dirname(path.realpath(__file__))
        tmx_file += '/data/{0}'.format(filename)

#        tmpfile = tempfile.NamedTemporaryFile()
#        po_filename = tmpfile.name + ".po"

        return tmx_file


    def test_convertion_omegat(self):
        SOURCE = "source.txt"
        TARGET = "target.txt"

        tmx_file = self._get_tmx_file('omegat.tmx')
        convertTmx = ConvertTmx(tmx_file, SOURCE, TARGET)
        convertTmx.convert("en", "ca")

        with open(SOURCE) as file:
            source_lines = file.readlines()

        with open(TARGET) as file:
            target_lines = file.readlines()

        self.assertEquals(source[0], '"Aligner" aligner utility')
        self.assertEquals(target[0], 'Alineador de textos "Aligner"')

if __name__ == '__main__':
    unittest.main()

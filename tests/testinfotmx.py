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

from src.tmx_to_text.infotmx import InfoTmx
import unittest
from os import path
import tempfile

class TestInfoTmx(unittest.TestCase):

    def _get_tmx_file(self, filename):
        tmx_file = path.dirname(path.realpath(__file__))
        tmx_file += '/data/{0}'.format(filename)
        return tmx_file


    def test_info_languages(self):

        tmx_file = self._get_tmx_file('simple.tmx')
        info = InfoTmx(tmx_file)
        languages = info.get_information()
        self.assertTrue("en" in languages)
        self.assertTrue("ca" in languages)
        self.assertEquals(1, languages["ca"])
        self.assertEquals(1, languages["en"])

if __name__ == '__main__':
    unittest.main()

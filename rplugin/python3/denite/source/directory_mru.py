"""
The original code of this file is
https://github.com/Shougo/neomru.vim/blob/master/rplugin/python3/denite/source/file_mru.py
and it is released under the MIT license.

Copyright (c) 2014 Shougo Matsushita <Shougo.Matsu at gmail.com>
Released under the MIT license
https://github.com/Shougo/neomru.vim/blob/master/LICENSE
"""

from .base import Base


class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = "directory_mru"
        self.kind = "directory"

    def gather_candidates(self, context):
        return [
            {"word": x, "action__path": x}
            for x in self.vim.eval(
                "neomru#_get_mrus().directory"
                '.gather_candidates([], {"is_redraw": 0})')]

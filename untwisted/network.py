# Copyright (C) 2011  Iury O. G. Figueiredo
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  USA
#
# Iury <robatsch@hotmail.com>


""" The untwisted core. """


from untwisted.usual import *
from untwisted.magic import *
from socket import *
from core import *
import core

class Spin(socket, Mode):
    def __init__(self, sock=None):
        socket.__init__(self, _sock = sock._sock if sock else None)
        Mode.__init__(self)

        #Registering itself.
        core.gear.register(self)

        self.setblocking(0) 

    def destroy(self):
        core.gear.unregister(self)
        self.base.clear()


_all__ = [
            'Spin', 
            'Stop',
            'Root',
            'Kill',
            'spawn',
            'core', 
            'hold',
            'xmap',
            'rmap',
            'imap',
            'cmap',
            'nmap',
            'mmap',
            'smap',
            'hook',
            'READ',
            'WRITE',
            'get_event',
            'zmap',
            'install_reactor'
          ]





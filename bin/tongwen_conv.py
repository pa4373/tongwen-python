#!/usr/bin/env python
#
# tongwen_conv
#
# Copyright (C) 2011 -  Wei-Ning Huang (AZ) <aitjcize@gmail.com>
# All Rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import sys
import getopt

from pyTongwen.conv import TongWenConv

# Program Information
program_name = 'tongwen_conv'
program_version = '0.1.0'


def abort(msg):
    """Print error message and abort program."""
    print >> sys.stderr, msg
    sys.exit(1)


def help():
    """Print help message."""
    print >> sys.stderr,\
'''usage: %s [-t type] [-i infile] [-o outfile]
       %s [-v] [-h]\n
       -t      Type of operation, either 'zhs' or 'zht'
       -i      Specify source filename, default is stdin
       -o      Specify destination filename, default is stdout
       -v      Show version info
       -h      Show this help list\n
Please report bugs to AZ Huang <aitjcize@gmail.com>'''\
    % (program_name, program_name)


def version():
    """Print version info."""
    print >> sys.stderr, \
'''%s Ver %s\n\
Copyright (C) 2009 AZ Huang (Wei-Ning Huang)
License GPLv2: GNU GPL version 2 <http://gnu.org/licenses/gpl-2.0.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.\n
Written by AZ Huang (Wei-Ning Huang).'''\
    % (program_name, program_version)


def main():
    """Perform conversion."""
    infile = sys.stdin
    outfile = sys.stdout
    op = 'zhs'

    try:
        optlist, args = getopt.getopt(sys.argv[1:], 'vht:i:o:')
    except getopt.GetoptError as i:
        abort('error: %s' % i.msg)

    for i in optlist:
        if i[0] == '-h':
            help()
            sys.exit(0)
        elif i[0] == '-v':
            version()
            sys.exit(0)
        elif i[0] == '-t':
            if i[1] != 'zhs' and i[1] != 'zht':
                abort("error: invalid parameter `%s'" % i[1])
            op = i[1]
        elif i[0] == '-i':
            try:
                infile = open(i[1], 'r')
            except IOError, e:
                abort('error: %s: %s' % (i[1], e))
        elif i[0] == '-o':
            try:
                outfile = open(i[1], 'w')
            except IOError, e:
                abort('error: %s: %s' % (i[1], e))
        else:
            # This should not happen
            sys.exit(1)

    tongwen = TongWenConv()
    data = infile.read()
    ret = tongwen.conv_zh(unicode(data, 'utf8'), op)
    outfile.write(ret.encode('utf8'))


if __name__ == '__main__':
    main()

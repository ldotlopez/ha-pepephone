# -*- coding: utf-8 -*-

# Copyright (C) 2022 Luis López <luis@cuarentaydos.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301,
# USA.


import argparse
import os

from . import PepeAPI, RequestError
from pprint import pprint as pp


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--username", default=os.environ.get("PEPEPHONE_USERNAME"), required=True
    )
    parser.add_argument(
        "-p", "--password", default=os.environ.get("PEPEPHONE_PASSWORD"), required=True
    )
    parser.add_argument("-n", "--number", required=True)

    args = parser.parse_args()

    api = PepeAPI()
    try:
        api.login(args.username, args.password)
        print(repr(api.get_data(args.number)))
    except RequestError as e:
        pp(e.kwargs["response"].content)

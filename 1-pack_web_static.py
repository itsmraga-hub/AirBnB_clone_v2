#!/usr/bin/python3
"""
    A Fabric script that generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo, using the function do_pack()
"""

from fabric.api import *
from datetime import datetime
import os


def do_pack():
    try:
        local("mkdir -p versions")
        f = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local("tar -zcvf {} web_static".format(f))
        return f
    except Exception:
        return None

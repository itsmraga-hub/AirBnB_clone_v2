#!/usr/bin/python3
"""
    A Fabric script that distributes an archive to your web servers, using
    the function do_deploy
"""

from fabric.api import *
import os
from datetime import datetime


env.hosts = ['52.91.127.250', '34.229.56.207']


def do_pack():
    try:
        local("mkdir -p versions")
        f = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local("tar -zcvf {} web_static".format(f))
        return f
    except Exception:
        return None


def do_deploy(archive_path):
    """
        do_deploy web static to server
        archive_path - path
    """
    try:
        file_name = archive_path.split("/")[-1]
        if not os.path.exists(archive_path):
            return False

        put(archive_path, '/tmp/')

        arch_file = os.path.basename(archive_path)
        arch_name = os.path.splittext(archive_file)[0]

        run("mkdir -p /data/web_static/releases/{}/".format(arch_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            arch_file, arch_name))

        run("rm /tmp/{}".format(arch_file))

        run("sudo rm -rf /data/web_static/current")

        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            archive_name))

        return True

    except Exception:
        return False


def deploy():
    """Creates and dist-s an archive file to the web servers"""
    arc_path = do_pack()
    if arc_path is None:
        return False
    return do_deploy(arc_path)


def do_clean(number=0):
    """Python script that deletes out of date archives"""
    pass

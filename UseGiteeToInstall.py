# -*- coding:utf-8 -*-
import git
from sys import platform as SystemPlatform
import tempfile

__author__ = "PartyParrot(__init__)"
TempDir = tempfile.TemporaryDirectory()

if SystemPlatform == 'darwin' or SystemPlatform == 'linux':
    CodeDir = git.Repo.clone_from(url='git@gitee.com:ky-studio/EasyPython.git', to_path=TempDir).git().working_dir
elif SystemPlatform == 'win32' or SystemPlatform == 'cygwin':
    CodeDir = git.Repo.clone_from(url='git@gitee.com:ky-studio/EasyPython.git', to_path=TempDir).git().working_dir

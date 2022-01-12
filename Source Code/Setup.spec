# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None

file = ['EasyShell.py']

for x in os.listdir("EasyScript"):
    if x == 'HelpDoc' or x == "config.yml" or x == "__pycache__":
        pass
    else:
        file.append(f"EasyScript/{x}")



a = Analysis(file,
             pathex=[],
             binaries=[],
             # datas=['EasyScript'],
             datas=[('EasyScript/config.yml', './EasyScript/'), ('EasyScript/HelpDoc/en-us.txt', './EasyScript/HelpDoc/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='EasyShell',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='EasyShell')

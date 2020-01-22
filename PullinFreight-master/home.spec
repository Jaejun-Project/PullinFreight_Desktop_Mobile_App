# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['home.py'],
             pathex=['/Users/jaejunmin/Desktop/CSCI401/TruckerTracker/Pullin_Freight_Standalone'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += [('truck_blue.png','./image/truck_blue.png', "DATA")]
a.datas += [('144x144.png','./image/144x144.png', "DATA")]
a.datas += [('512x512.png','./image/512x512.png', "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='home',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

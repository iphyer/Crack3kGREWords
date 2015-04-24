# -*- mode: python -*-
a = Analysis(['D:\\SRC\\ZYNM3k.py'],
             pathex=['C:\\Python27\\PyInstaller-2.1\\ZYNM3k'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='ZYNM3k.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='D:\\SRC\\icon.ico')

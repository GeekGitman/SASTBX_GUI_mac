# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Applications/SASTBX1.0.1/gui/sasqt/homemain.py'],
             pathex=['/opt/local/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages', '/Applications/SASTBX1.0.1/gui/sasqt'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='homemain',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='/Applications/SASTBX1.0.1/gui/sasqt/molecule.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='homemain')
app = BUNDLE(coll,
             name='homemain.app',
             icon='/Applications/SASTBX1.0.1/gui/sasqt/molecule.icns',
             bundle_identifier=None)

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\OPENDATA\\Desktop\\Lucas\\Projetos\\Projeto - APP Investimento Python'],
             binaries=[],
             datas=[('C:\\Users\\OPENDATA\\Desktop\\Lucas\\Projetos\\Projeto - APP Investimento Python\\investimentos.json', '.'), ('C:\\Users\\OPENDATA\\Desktop\\Lucas\\Projetos\\Projeto - APP Investimento Python\\4-wheeler-dealer.wav', '.')],
             hiddenimports=[],
             hookspath=[],
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
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='app')

# -*- mode: python -*-

block_cipher = None


a = Analysis(['cue-csgo.py'],
             pathex=['C:\\Users\\nicko\\Google Drev\\cosairlib'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=None,
             win_no_prefer_redirects=None,
             win_private_assemblies=None,
             cipher=block_cipher)

a.datas += [('cue_csgo\\resources\\CUESDK.x64_2013.dll','cue_csgo\\resources\\CUESDK.x64_2013.dll','DATA')]
a.datas += [('cue_csgo\\resources\\cue-cs.xpm','cue_csgo\\resources\\cue-cs.xpm','DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='CUE_gamestate.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False)

from kivy_deps import sdl2, glew



# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['calculator.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

a.datas +=[('code\calc.kv','E:\\Mahmoud\\01 programming cources\\006 python\\kivy cources\\My Apps\\Calculater\calc.kv'),'DATA']


exe = EXE(Tree('E:\\Mahmoud\\01 programming cources\\006 python\\kivy cources\\My Apps\\Calculater\\')),
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins+glew.dep_bins) ],
    name='calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

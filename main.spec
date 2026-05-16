# main.spec
a = Analysis(
    ['main.py'],
    pathex=['.'],
    datas=[('datosAnios.xlsx', '.')],  # incluye el Excel
    hiddenimports=['pandas', 'matplotlib', 'openpyxl'],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    name='trazador-cubico',
    console=True,
    onefile=True,
)
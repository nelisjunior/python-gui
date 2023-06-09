# https://cx-freeze.readthedocs.io/en/latest/setup_script.html#setup-script

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('apache_gui.py', base=base)
]

setup(name='apache_manage_gui',
      version = '0.1',
      description = 'Gerenciador de arquivos do apache no Windows11',
      options = {'build_exe': build_options},
      executables = executables)


from setuptools import setup

APP = ['seo_optimizer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'tkinter', 'random', 'urllib', 'webbrowser'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

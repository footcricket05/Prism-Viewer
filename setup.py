from setuptools import setup, find_packages

def main():
    from main import PrismViewer
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    viewer = PrismViewer()
    viewer.show()
    sys.exit(app.exec_())

setup(
    name='prism_viewer',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'PyQt5',
        'numpy',
    ],
    entry_points={
        'gui_scripts': [  
            'prism-viewer=main:main',
        ],
    },
)

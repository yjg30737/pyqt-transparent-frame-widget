from setuptools import setup, find_packages

setup(
    name='pyqt-transparent-frame-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt widget(window) which has transparent frame(title bar)',
    url='https://github.com/yjg30737/pyqt-transparent-frame-widget.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-frameless-window @ git+https://git@github.com/yjg30737/pyqt-frameless-window.git@main'
    ]
)
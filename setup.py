from setuptools import setup, find_packages

setup(
    name='pyqt-new-window-handler',
    version='0.2.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QObject type class which operates/handles "New Window" feature',
    url='https://github.com/yjg30737/pyqt-new-window-handler.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-custom-titlebar-setter>=0.0.1',
        'pyqt-custom-titlebar-window>=0.0.1'
    ]
)
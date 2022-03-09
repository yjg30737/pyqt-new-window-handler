from setuptools import setup, find_packages

setup(
    name='pyqt-new-window-handler',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt QObject type class which operates/handles "New Window" feature',
    url='https://github.com/yjg30737/pyqt-new-window-handler.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main'
    ]
)
from setuptools import setup

setup(
    name='quote-gui',
    version='1.0.0',
    packages=['quote_gui'],
    url='https://github.com/brendoser/quote-gui',
    license='',
    author='brenden.dielissen',
    author_email='brendendielissen@gmail.com',
    description='A GUI for displaying quotes from books on Amazon.',
    install_requires=['Pillow>=8.2.0', 'tk>=0.1.0'],
    entry_points={
        'console_scripts': ['quote-gui=quote_gui.main_window:main']
    },
    include_package_data=True
)

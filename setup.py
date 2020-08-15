from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
        name='notes',
        version='0.1.0',
        author="Penalty Double",
        author_email="2notrump@gmail.com",
        description="A simple notes webapp.",
        long_description=long_description,
        long_description_content_type='text/markdown',
        uri='https://github.com/penaltydbl/notes',
        packages=find_packages('src'),
        package_dir={'': '.'},
        install_requires=['flask'],
        python_requires='>=3.6',
        entry_points={
        'console_scripts': [
            'notes=notes.__init__:create_app',
           ],
        }
 )

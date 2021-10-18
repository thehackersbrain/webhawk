from setuptools import setup, find_packages
from webhawk import __version__

with open('README.md') as readme:
    long_description = readme.read().strip()


setup(
    name='webhawk',
    version=__version__,
    description='Web Recon Framework',
    author='Gaurav Raj',
    url='https://github.com/thehackersbrain/webhawk',
    author_email='techw803@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['webhawk', 'web', 'recon', 'hacking',
              'python3', 'python', 'thehackersbrain', 'gaurav raj'],
    packages=find_packages(),
    package_data={"": ["data/*"]},
    install_requires=['requests', 'rich', 'bs4'],
    entry_points={'console_scripts': ['webhawk=webhawk.src.__main__:main']},
    zip_safe=False,
)

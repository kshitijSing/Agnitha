import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))

setup(
      name = 'spoken_english_to_written_english',
      packages = ['spoken_english_to_written_english'],
      version='0.1',
      license=open('LICENSE.txt').read(),
      description='Spoken english to written english conversion system',
      author='Kshitij Gangwar',
      author_email='201751021@iiitvadodara.ac.in',
      url='https://github.com/kshitijSing/Agnitha',
     )

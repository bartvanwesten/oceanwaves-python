from setuptools import setup, find_packages

setup(
    name='oceanwaves',
    version='1.0.0rc6',
    author='Bas Hoonhout',
    author_email='bas.hoonhout@deltares.nl',
    url='http://oceanwaves.readthedocs.io/',
    license='MIT',
    description='A toolbox for ocean wave datasets',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
    keywords=['ocean waves oceanwaves swan waverider wavedroid xarray'],
    packages=find_packages(exclude=['docs', 'data', 'notebooks', 'tests', 'cover']),
    python_requires='>=2.7, <4',
    install_requires=[
        'docopt',
        'xarray',
        'scipy',
        'numpy',
    ],
)

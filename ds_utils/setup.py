import setuptools
setuptools.setup(
     name='foster_ds_utils',  
     version='0.1',
     scripts=['foster_ds_utils'] ,
     author="Ben Wolfson",
     author_email="bwolfson@alumni.princeton.edu",
     description="Package for Foster's class containing useful functions",
     long_description="Package for Foster's class containing useful functions",
     long_description_content_type="text/markdown",
     url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
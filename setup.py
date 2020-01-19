import setuptools
setuptools.setup(
     name='foster2020',  
     version='0.1',
     scripts=['foster2020/foster2020'] ,
     author="Ben Wolfson",
     author_email="bwolfson@alumni.princeton.edu",
     description="Package for Foster's class containing useful functions",
     long_description="Package for Foster's class containing useful functions",
     long_description_content_type="text/markdown",
     url="https://github.com/bwolfson2/foster_2020",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
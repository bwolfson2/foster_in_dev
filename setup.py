import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
     name='foster2020',  
     version='0.1',
     scripts=['foster2020/foster2020'] ,
     author="Ben Wolfson",
     author_email="bwolfson@alumni.princeton.edu",
     description="Package for Foster's class containing useful functions",
     long_description=readme(),
     long_description_content_type="text/markdown",
     url="https://github.com/bwolfson2/foster2020",
     packages=setuptools.find_packages(),
     install_requires = ["seaborn","matplotlib","numpy","chardet","html2text","pandas","scikit_learn"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
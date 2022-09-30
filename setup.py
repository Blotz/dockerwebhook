from setuptools import setup

if __name__=="__main__":
    setup(
        name='dockerwebhook',
        version='1.0.0',
        description="Docker webhook listener",
        url="https://github.com/Blotz/dockerwebhook",
        author="Ferdinand Theil",
        author_email="f.p.theil@gmail.com",
        license="GPL-3.0",
        packages=["dockerwebhook"],
        install_requires=["flask", "docker-py", "waitress"]
    )

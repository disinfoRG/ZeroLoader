from setuptools import setup

setup(
    name="zeroloader",
    version="v0.1.0",
    description="read 0archive's public dataset",
    url="https://github.com/disinfoRG/ZeroLoader.git",
    packages=["zeroloader"],
    install_requires=["python-dotenv", "google-api-python-client", "google-auth",
                      "google-auth-httplib2", "google-auth-oauthlib", "oauth2client",
                      "pandas"],
    python_requires=">=3.5",
    license="MIT",
    zip_safe=False,
)
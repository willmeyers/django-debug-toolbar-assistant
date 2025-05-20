from setuptools import setup


setup(
    name="django-debug-toolbar-assistant",
    version="0.1",
    packages=["django_debug_toolbar_assistant_panel"],
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "django-debug-toolbar>=4.0",
        "google-cloud-aiplatform>=1.40",
    ],
)

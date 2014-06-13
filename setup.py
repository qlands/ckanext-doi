from setuptools import setup, find_packages

version = '0.1'

setup(
	name='ckanext-doi',
	version=version,
	description='CKAN extension for assigning a DOI to datasets',
	classifiers=[],
	keywords='',
	author='Ben Scott',
	author_email='ben@benscott.co.uk',
	url='',
	license='',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['ckanext', 'ckanext.doi'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[],
	entry_points=\
	"""
    [ckan.plugins]
    	contact=ckanext.doi.plugin:DOIPlugin
	""",
)
from setuptools import setup, find_packages


setup(
    name='pvader',
    version='2.0.0',
    description='Análise de Sentimentos em Português',
    long_description="LeIA (Léxico para Inferência Adaptada) é um fork do léxico e ferramenta para análise de sentimentos VADER (Valence Aware Dictionary and sEntiment Reasoner) adaptado para textos em português, com suporte para emojis e foco na análise de sentimentos de textos expressos em mídias sociais - mas funcional para textos de outros domínios.",
    url='https://github.com/pguatura/LeIA/',
    author='rafjaa',
    license='MIT',
    classifiers=[
        'Development Status :: Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License'
    ],
    package_data={'': ['pvader/lexicons']},
    include_package_data=True,
    install_requires=[
    ],
    packages=find_packages(include=["pvader","pvader/lexicons"]),
)

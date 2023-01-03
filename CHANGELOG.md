# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2023-01-03
- Agregada la linea
  <code>python -m pip install --force-reinstall "cryptography==38.0.4"</code>
 a 
  <code>pipelines/PIPELINE-FULL-PRODUCTION/setup.sh </code>
  para resolver un problema de dependencias en el deployment de produccion

- Agregada la configuracion de los s3 buckets al archivo samconfig.toml de SAM para staging y production

## [1.0.0] - 2021-01-08
### Added
- Versión inicial de código.


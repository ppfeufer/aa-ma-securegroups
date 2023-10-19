# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## \[In Development\]

## \[0.6.0\] - 2023-10-19

### Added

- Support for corporation role filter (Thanks to @ErikKalkoken)
- Character type selector to skill set filter (This allows to create auto groups for
  something like fax alts) (Thanks to @ErikKalkoken)

### Fixed

- Capitalization for translatable strings

### Changed

- Page load of asset filter form improved (Thanks to @ErikKalkoken)
- Performance of asset and compliance filters improved (Thanks to @ErikKalkoken)
- Dependency to Member Audit
  - `aa-memberaudit>=3.3.1`
- Translations updated

## \[0.5.0\] - 2023-10-05

This release is made to be on par with the original app, which is no longer
maintained. To switch to this maintained version, see [Migrating from Member Audit Securegroups](https://github.com/ppfeufer/aa-memberaudit-secure-groups#step-05-migrating-from-member-audit-securegroups).

### Added

- Korean translation

### Fixed

- Capitalization for translatable strings

## \[0.4.0\] - 2023-08-15

### Added

- Names of missing characters when the compliance filter fails
- Spanish translation

### Changed

- Moved the build process to PEP 621 / pyproject.toml
- Character names sorted alphabetically in all filters

## \[0.3.0\] - 2023-05-31

### Fixed

- Migration dependency for Member Audit >= 2.0.0

### Changed

- Dependencies:
  - `aa-memberaudit>=2.0.0`
  - `allianceauth>=3.0.0`
  - `allianceauth-securegroups>=0.5.1`

## \[0.2.0\] - 2023-02-27

### Added

- Secure Group's audit filter to the filters for better visual feedback

## \[0.1.0\] - 2022-08-06

### Fixed

- Compatibility to the Member Audit >=1.15.1 and its changes to the `Character` model

### Added

- Makefile
- Editorconfig

### Changed

- Several configs updated
- Requirements
  - `allianceauth>=2.15.1`
  - `aa-memberaudit>=1.15.1`
  - `allianceauth-securegroups>=0.2.1`
  - `python>=3.8`

### Removed

- Unused files

## \[0.1.0a3\] - 2021-01-16

### Fixed

- Bug involving skillpoint filter

## \[0.1.0a2\] - 2021-01-05

### Added

- Activity Filter
- Age Filter
- Skill Point Filter

### Changed

- Improved Admin Panel

## \[0.1.0a1\] - 2021-01-05

### Added

- Initial Release

# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Critical content demanding immediate user attention due to potential risks.
-->

## \[In Development\] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

### Added

- Proper filter names
- Reversed logic to compliance filter (optional)

## Changed

- Switch to `django-solo` to provide the singleton for the compliance model, instead of the custom implementation
- Several code improvements

## \[1.2.0\] - 2024-10-10

### Changed

- Dependencies updated
  - `allianceauth`>=4.3.1
  - `aa-memberaudit`>=3.10.0
- Japanese translation improved
- Lingua codes updated to match Alliance Auth v4.3.1

## \[1.1.0\] - 2024-07-27

### Added

- Prepared Czech translation for when Alliance Auth supports it

### Changed

- French translation improved
- Russian translation improved

### Removed

- Support for Python 3.8 and Python 3.9

## \[1.0.1\] - 2024-05-16

### Changed

- Translations updated

## \[1.0.0\] - 2024-03-16

> \[!NOTE\]
>
> **This version needs at least Alliance Auth v4.0.0!**
>
> Please make sure to update your Alliance Auth instance **before**
> you install this version, otherwise, an update to Alliance Auth will
> be pulled in unsupervised.

### Added

- Corp title filter (Thanks to @ErikKalkoken)
- Time in corp filter (Thanks to @ErikKalkoken)
- Compatibility to Alliance Auth v4

### Removed

- Compatibility to Alliance Auth v3

## \[0.6.1\] - 2023-10-22

> \[!NOTE\]
>
> **This is the last version compatible with Alliance Auth v3.**

### Fixed

- Smart Group failed to process when filter requirements are not met

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
maintained. To switch to this maintained version, see [Migrating from Member Audit Securegroups](https://github.com/ppfeufer/aa-ma-securegroups#step-05-migrating-from-member-audit-securegroups).

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

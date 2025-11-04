# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog] and this project adheres to [Semantic Versioning].

<!--
GitHub MD Syntax:
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

Highlighting:
https://docs.github.com/assets/cb-41128/mw-1440/images/help/writing/alerts-rendered.webp

> [!NOTE]
> Highlights information that users should take into account, even when skimming.

> [!TIP]
> Optional information to help a user be more successful.

> [!IMPORTANT]
> Crucial information necessary for users to succeed.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advised about risks or negative outcomes of certain actions.
-->

## [In Development] - Unreleased

<!--
Section Order:

### Added
### Fixed
### Changed
### Deprecated
### Removed
### Security
-->

<!-- Your changes go here -->

## [1.6.1] - 2025-11-04

### Fixed

- Django `makemessages` seems to be ignoring f-strings now

### Changed

- Translations updated

## [1.6.0] - 2025-08-05

### Added

- Home Station (Death Clone) smart filter

### Changed

- Translations updated

## [1.5.2] - 2025-06-03

### Changed

- Translations updated

## [1.5.1] - 2025-05-05

### Changed

- Translations updated

## [1.5.0] - 2025-01-06

### Added

- End date to the `TimeInCorporationFilter` for reverse logic

### Changed

- Filter messages made translatable

## [1.4.0] - 2024-12-31

### Added

- Checkbox to reverse logic for `TimeInCorporationFilter`, which comes in handy
  when you want to put characters that are not in the corporation for a
  certain amount of time in a group, like for a probation period.

## [1.3.1] - 2024-12-14

### Added

- Python 3.13 to the test matrix

### Changed

- Simplify code for `ComplianceFilter.audit_filter` logic
- Translations updated

## [1.3.0] - 2024-12-06

### Added

- Proper filter names
- Reversed logic to compliance filter (optional)
- Testing for Python 3.13

### Changed

- Several code improvements

## [1.2.0] - 2024-10-10

### Changed

- Dependencies updated
  - `allianceauth`>=4.3.1
  - `aa-memberaudit`>=3.10.0
- Japanese translation improved
- Lingua codes updated to match Alliance Auth v4.3.1

## [1.1.0] - 2024-07-27

### Added

- Prepared Czech translation for when Alliance Auth supports it

### Changed

- French translation improved
- Russian translation improved

### Removed

- Support for Python 3.8 and Python 3.9

## [1.0.1] - 2024-05-16

### Changed

- Translations updated

## [1.0.0] - 2024-03-16

> [!NOTE]
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

## [0.6.1] - 2023-10-22

> [!NOTE]
>
> **This is the last version compatible with Alliance Auth v3.**

### Fixed

- Smart Group failed to process when filter requirements are not met

## [0.6.0] - 2023-10-19

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

## [0.5.0] - 2023-10-05

This release is made to be on par with the original app, which is no longer
maintained. To switch to this maintained version, see [Migrating from Member Audit Securegroups](https://github.com/ppfeufer/aa-ma-securegroups#step-05-migrating-from-member-audit-securegroups).

### Added

- Korean translation

### Fixed

- Capitalization for translatable strings

## [0.4.0] - 2023-08-15

### Added

- Names of missing characters when the compliance filter fails
- Spanish translation

### Changed

- Moved the build process to PEP 621 / pyproject.toml
- Character names sorted alphabetically in all filters

## [0.3.0] - 2023-05-31

### Fixed

- Migration dependency for Member Audit >= 2.0.0

### Changed

- Dependencies:
  - `aa-memberaudit>=2.0.0`
  - `allianceauth>=3.0.0`
  - `allianceauth-securegroups>=0.5.1`

## [0.2.0] - 2023-02-27

### Added

- Secure Group's audit filter to the filters for better visual feedback

## [0.1.0] - 2022-08-06

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

## [0.1.0a3] - 2021-01-16

### Fixed

- Bug involving skillpoint filter

## [0.1.0a2] - 2021-01-05

### Added

- Activity Filter
- Age Filter
- Skill Point Filter

### Changed

- Improved Admin Panel

## [0.1.0a1] - 2021-01-05

### Added

- Initial Release

<!-- Links to be updated upon release -->

[0.1.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.1.0a3...v0.1.0 "v0.1.0"
[0.1.0a1]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/commits/v0.1.0a1 "v0.1.0a1"
[0.1.0a2]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.1.0a1...v0.1.0a2 "v0.1.0a2"
[0.1.0a3]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.1.0a2...v0.1.0a3 "v0.1.0a3"
[0.2.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.1.0...v0.2.0 "v0.2.0"
[0.3.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.2.0...v0.3.0 "v0.3.0"
[0.4.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.3.0...v0.4.0 "v0.4.0"
[0.5.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.4.0...v0.5.0 "v0.5.0"
[0.6.0]: https://gitlab.com/eclipse-expeditions/aa-memberaudit-securegroups/-/compare/v0.5.0...v0.6.0 "v0.6.0"
[0.6.1]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v0.6.0...v0.6.1 "v0.6.1"
[1.0.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v0.6.1...v1.0.0 "v1.0.0"
[1.0.1]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.0.0...v1.0.1 "v1.0.1"
[1.1.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.0.1...v1.1.0 "v1.1.0"
[1.2.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.1.0...v1.2.0 "v1.2.0"
[1.3.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.2.0...v1.3.0 "v1.3.0"
[1.3.1]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.3.0...v1.3.1 "v1.3.1"
[1.4.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.3.1...v1.4.0 "v1.4.0"
[1.5.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.4.0...v1.5.0 "v1.5.0"
[1.5.1]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.5.0...v1.5.1 "v1.5.1"
[1.5.2]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.5.1...v1.5.2 "v1.5.2"
[1.6.0]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.5.2...v1.6.0 "v1.6.0"
[1.6.1]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.6.0...v1.6.1 "v1.6.1"
[in development]: https://github.com/ppfeufer/aa-ma-securegroups/compare/v1.6.1...HEAD "In Development"
[keep a changelog]: http://keepachangelog.com/ "Keep a Changelog"
[semantic versioning]: http://semver.org/ "Semantic Versioning"

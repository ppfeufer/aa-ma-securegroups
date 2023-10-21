# Member Audit Secure Groups Integration for Alliance Auth<a name="member-audit-secure-groups-integration-for-alliance-auth"></a>

[![Version](https://img.shields.io/pypi/v/aa-ma-securegroups?label=release)](https://pypi.org/project/aa-ma-securegroups/)
[![License](https://img.shields.io/github/license/ppfeufer/aa-ma-securegroups)](https://github.com/ppfeufer/aa-ma-securegroups/blob/master/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/aa-ma-securegroups)](https://pypi.org/project/aa-ma-securegroups/)
[![Django](https://img.shields.io/pypi/djversions/aa-ma-securegroups?label=django)](https://pypi.org/project/aa-ma-securegroups/)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/ppfeufer/aa-ma-securegroups/master.svg)](https://results.pre-commit.ci/latest/github/ppfeufer/aa-ma-securegroups/master)
[![Code Style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](http://black.readthedocs.io/en/latest/)
[![Discord](https://img.shields.io/discord/790364535294132234?label=discord)](https://discord.gg/zmh52wnfvM)
[![Checks](https://github.com/ppfeufer/aa-ma-securegroups/actions/workflows/automated-checks.yml/badge.svg)](https://github.com/ppfeufer/aa-ma-securegroups/actions/workflows/automated-checks.yml)
[![codecov](https://codecov.io/gh/ppfeufer/aa-ma-securegroups/branch/master/graph/badge.svg)](https://codecov.io/gh/ppfeufer/aa-ma-securegroups)
[![Translation status](https://weblate.ppfeufer.de/widget/alliance-auth-apps/aa-member-audit-secure-groups/svg-badge.svg)](https://weblate.ppfeufer.de/engage/alliance-auth-apps/)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/ppfeufer/aa-ma-securegroups/blob/master/CODE_OF_CONDUCT.md)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N8CL1BY)

This is an integration between [Member Audit](https://gitlab.com/ErikKalkoken/aa-memberaudit) and [Secure Groups](https://github.com/pvyParts/allianceauth-secure-groups) for [Alliance Auth](https://gitlab.com/allianceauth/allianceauth) (AA).

______________________________________________________________________

<!-- mdformat-toc start --slug=gitlab --maxlevel=6 --minlevel=1 -->

- [Member Audit Secure Groups Integration for Alliance Auth](#member-audit-secure-groups-integration-for-alliance-auth)
  - [What's the difference to Member Audit Securegroups](#whats-the-difference-to-member-audit-securegroups)
  - [Features](#features)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Step 0.5 - Migrating from Member Audit Securegroups](#step-05-migrating-from-member-audit-securegroups)
    - [Step 1 - Install the Package](#step-1-install-the-package)
    - [Step 2 - Config](#step-2-config)
    - [Step 3 - Finalize App Installation](#step-3-finalize-app-installation)
  - [Filters](#filters)
  - [Changelog](#changelog)
  - [Translation Status](#translation-status)
  - [Contributing](#contributing)

<!-- mdformat-toc end -->

______________________________________________________________________

## What's the difference to Member Audit Securegroups<a name="whats-the-difference-to-member-audit-securegroups"></a>

Pretty much nothing.

I took over Member Audit Securegroups in August 2022 from the original developer who
is no longer actively maintaining the app. After more than a year and the fact that
the original developer didn't want to transfer the PyPi repo to me, I decided it is
time to make an actual fork of the app which is now again actively maintained by me.

This app is fully compatible with the original, all that has changed is the `pip`
name from `aa-memberaudit-securegroups` to `aa-ma-securegroups`, and if
you had the original app installed, it is really easy to switch to this one, see
[Step 0.5 - Migrating from Member Audit Securegroups](#step-05-migrating-from-member-audit-securegroups).

## Features<a name="features"></a>

- Activity Filter
- Asset Filter
- Character Age Filter
- Compliance Filter
- Skill Set Filter
- Skill Point Filter

## Installation<a name="installation"></a>

### Requirements<a name="requirements"></a>

This integration needs [Member Audit](https://gitlab.com/ErikKalkoken/aa-memberaudit)
and [Secure Groups](https://github.com/pvyParts/allianceauth-secure-groups) to
function. Please make sure they are installed before continuing.

### Step 0.5 - Migrating from Member Audit Securegroups<a name="step-05-migrating-from-member-audit-securegroups"></a>

In case you have the original app installed, you need to uninstall it before
you can continue. To do so, simply run:

```shell
pip uninstall aa-memberaudit-securegroups
```

That's all, no need to worry about the DB related stuff, this app is fully
compatible with it and will use the DB tables from the original app. Now feel free
to continue with the installation.

### Step 1 - Install the Package<a name="step-1-install-the-package"></a>

Make sure you are in the virtual environment (venv) of your Alliance Auth
installation. Then install the newest release from PyPI:

```shell
pip install aa-ma-securegroups
```

### Step 2 - Config<a name="step-2-config"></a>

Add `memberaudit_securegroups` to your `INSTALLED_APPS`.

### Step 3 - Finalize App Installation<a name="step-3-finalize-app-installation"></a>

Run migrations:

```shell
python manage.py migrate
```

Restart your supervisor services for Auth

## Filters<a name="filters"></a>

| Filter Name             | Matches if...                                                                  |
| ----------------------- | ------------------------------------------------------------------------------ |
| Activity Filter         | User has *at least one* character active within the last X days                |
| Age Filter              | User has *at least one* character over X days old                              |
| Asset Filter            | User has *at least one* character with *any of* the assets defined             |
| Compliance Filter       | User has *all* characters registered on Member Audit                           |
| Corporation Role Filter | User has a character (main or alt) in a certain corpration with a certain role |
| Skill Point Filter      | User has *at least one* character with at least X skill points                 |
| Skill Set Filter        | User has *at least one* character with *any of* the selected skill sets        |

## Changelog<a name="changelog"></a>

See [CHANGELOG.md]

## Translation Status<a name="translation-status"></a>

[![Translation status](https://weblate.ppfeufer.de/widget/alliance-auth-apps/aa-intel-tool/multi-auto.svg)](https://weblate.ppfeufer.de/engage/alliance-auth-apps/)

Do you want to help translate this app into your language or improve the existing
translation? - [Join our team of translators][weblate engage]!

## Contributing<a name="contributing"></a>

Do you want to contribute to this project? That's cool!

Please make sure to read the [Contribution Guidelines].\
(I promise, it's not much, just some basics)

<!-- Inline links -->

[changelog.md]: https://github.com/ppfeufer/aa-ma-securegroups/blob/master/CHANGELOG.md
[contribution guidelines]: https://github.com/ppfeufer/aa-ma-securegroups/blob/master/CONTRIBUTING.md "Contribution Guidelines"
[weblate engage]: https://weblate.ppfeufer.de/engage/alliance-auth-apps/ "Weblate Translations"

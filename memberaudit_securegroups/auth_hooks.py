"""
Hook into Alliance Auth
"""

# Alliance Auth
from allianceauth import hooks

# Memberaudit Securegroups
from memberaudit_securegroups.models import (
    ActivityFilter,
    AgeFilter,
    AssetFilter,
    ComplianceFilter,
    SkillPointFilter,
    SkillSetFilter,
)


@hooks.register("secure_group_filters")
def filters():
    return [
        ActivityFilter,
        AgeFilter,
        AssetFilter,
        ComplianceFilter,
        SkillPointFilter,
        SkillSetFilter,
    ]

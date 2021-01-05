from allianceauth import hooks

from .models import (
    MemberAuditActivityFilter,
    MemberAuditAgeFilter,
    MemberAuditAssetFilter,
    MemberAuditComplianceFilter,
    MemberAuditSkillPointFilter,
    MemberAuditSkillSetFilter,
)


@hooks.register("secure_group_filters")
def filters():
    return [
        MemberAuditActivityFilter,
        MemberAuditAgeFilter,
        MemberAuditAssetFilter,
        MemberAuditComplianceFilter,
        MemberAuditSkillPointFilter,
        MemberAuditSkillSetFilter,
    ]

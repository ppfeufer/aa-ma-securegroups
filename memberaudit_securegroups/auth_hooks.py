from allianceauth import hooks

from .models import MemberAuditComplianceFilter


@hooks.register("secure_group_filters")
def filters():
    return [MemberAuditComplianceFilter]

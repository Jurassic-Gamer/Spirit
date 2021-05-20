from dataclasses import dataclass

@dataclass
class AuditData:
    msg_id: str
    user_name: str
    user_id: str
    activity: str
    timestamp: str
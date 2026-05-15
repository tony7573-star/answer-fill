from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class AuditEvent:
    exam_id: str
    actor: str
    action: str
    payload: dict
    created_at: str

    @classmethod
    def create(cls, exam_id: str, actor: str, action: str, payload: dict) -> "AuditEvent":
        return cls(
            exam_id=exam_id,
            actor=actor,
            action=action,
            payload=payload,
            created_at=datetime.now(timezone.utc).isoformat(),
        )

    def digest(self) -> str:
        body = json.dumps(asdict(self), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(body.encode("utf-8")).hexdigest()

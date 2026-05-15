from __future__ import annotations

from dataclasses import asdict, dataclass

from .answer_grid import AnswerGrid
from .audit import AuditEvent


@dataclass(frozen=True)
class ExtractionResult:
    exam_id: str
    page_count: int
    answers: tuple[str, ...]
    mean_confidence: float
    low_confidence_questions: tuple[int, ...]

    @property
    def needs_review(self) -> bool:
        return self.mean_confidence < 0.985 or bool(self.low_confidence_questions)


def build_audit_payload(result: ExtractionResult, reviewer: str = "system") -> dict:
    grid = AnswerGrid.from_tokens(result.exam_id, result.answers)
    event = AuditEvent.create(
        exam_id=result.exam_id,
        actor=reviewer,
        action="answer_grid_extracted",
        payload={
            "page_count": result.page_count,
            "answer_count": len(grid.answers),
            "mean_confidence": result.mean_confidence,
            "low_confidence_questions": list(result.low_confidence_questions),
            "needs_review": result.needs_review,
        },
    )
    payload = asdict(event)
    payload["digest"] = event.digest()
    return payload

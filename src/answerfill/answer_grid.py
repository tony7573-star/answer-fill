from __future__ import annotations

from dataclasses import dataclass


CIRCLED_TO_DIGIT = {
    "①": "1",
    "②": "2",
    "③": "3",
    "④": "4",
    "⑤": "5",
    "⑴": "1",
    "⑵": "2",
    "⑶": "3",
    "⑷": "4",
    "⑸": "5",
}


def normalize_answer_token(raw: str) -> str:
    token = str(raw or "").strip()
    if not token:
        raise ValueError("answer token is empty")
    token = CIRCLED_TO_DIGIT.get(token, token)
    if token not in {"1", "2", "3", "4", "5"}:
        raise ValueError(f"unsupported answer token: {raw!r}")
    return token


@dataclass(frozen=True)
class AnswerGrid:
    exam_id: str
    answers: tuple[str, ...]

    @classmethod
    def from_tokens(cls, exam_id: str, tokens: list[str] | tuple[str, ...]) -> "AnswerGrid":
        normalized = tuple(normalize_answer_token(token) for token in tokens)
        if len(normalized) == 0:
            raise ValueError("answer grid requires at least one answer")
        return cls(exam_id=exam_id, answers=normalized)

    def diff(self, other: "AnswerGrid") -> list[dict[str, str | int]]:
        max_len = max(len(self.answers), len(other.answers))
        changes: list[dict[str, str | int]] = []
        for idx in range(max_len):
            left = self.answers[idx] if idx < len(self.answers) else ""
            right = other.answers[idx] if idx < len(other.answers) else ""
            if left != right:
                changes.append({"question": idx + 1, "before": left, "after": right})
        return changes

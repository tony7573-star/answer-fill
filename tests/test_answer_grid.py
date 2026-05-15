import unittest

from answerfill import AnswerGrid, ExtractionResult, build_audit_payload, normalize_answer_token


class AnswerGridTest(unittest.TestCase):
    def test_normalizes_circled_numbers(self):
        self.assertEqual(normalize_answer_token("①"), "1")
        self.assertEqual(normalize_answer_token("⑤"), "5")

    def test_grid_diff_is_question_indexed(self):
        before = AnswerGrid.from_tokens("exam-1", ["①", "②", "③"])
        after = AnswerGrid.from_tokens("exam-1", ["1", "4", "3"])
        self.assertEqual(before.diff(after), [{"question": 2, "before": "2", "after": "4"}])

    def test_audit_payload_is_deterministic_shape(self):
        result = ExtractionResult(
            exam_id="exam-1",
            page_count=12,
            answers=("1", "2", "3"),
            mean_confidence=0.997,
            low_confidence_questions=(),
        )
        payload = build_audit_payload(result)
        self.assertEqual(payload["action"], "answer_grid_extracted")
        self.assertEqual(payload["payload"]["answer_count"], 3)
        self.assertFalse(payload["payload"]["needs_review"])
        self.assertEqual(len(payload["digest"]), 64)


if __name__ == "__main__":
    unittest.main()

import re

from database.models import CourtDecision
from parsers.regex_patterns import (
    DECISION_NUMBER_PATTERN,
    DATE_PATTERN,
    CASE_NUMBER_PATTERN,
    LOCATION_PATTERN,
    JUDGE_PATTERN
)


class DecisionParser:

    @staticmethod
    def find(pattern: str, text: str) -> str:
        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

        return "Не найдено"

    def parse(self, text: str, filename: str) -> CourtDecision:

        decision_number = self.find(
            DECISION_NUMBER_PATTERN,
            text
        )

        decision_date = self.find(
            DATE_PATTERN,
            text
        )

        case_number = self.find(
            CASE_NUMBER_PATTERN,
            text
        )

        location = self.find(
            LOCATION_PATTERN,
            text
        )

        judge = self.find(
            JUDGE_PATTERN,
            text
        )

        return CourtDecision(
            decision_number=decision_number,
            decision_date=decision_date,
            case_number=case_number,
            location=location,
            judge=judge,
            source_file=filename
        )
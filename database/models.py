from dataclasses import dataclass


@dataclass
class CourtDecision:
    decision_number: str
    decision_date: str
    case_number: str
    location: str
    judge: str
    source_file: str
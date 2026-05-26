DECISION_NUMBER_PATTERN = r"(?:РЕШЕНИЕ|Решение)\s*№?\s*([\w\-\/]+)"

DATE_PATTERN = (
    r"(\d{1,2}\s+[а-яА-Я]+\s+\d{4}\s+года)"
)

CASE_NUMBER_PATTERN = (
    r"(?:Дело|дело)\s*№\s*([\w\-\/]+)"
)

LOCATION_PATTERN = (
    r"г\.\s*([А-Яа-я\- ]+)"
)

JUDGE_PATTERN = (
    r"(?:Судья|судья)\s*([А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ]\.[А-ЯЁ]\.)?)"
)
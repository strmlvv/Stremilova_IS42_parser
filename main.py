from utils.file_reader import (
    get_word_files,
    read_file
)

from parsers.decision_parser import (
    DecisionParser
)

from database.db import (
    Session,
    DecisionDB
)


FOLDER_PATH = "parsed_decisions"


def main():

    parser = DecisionParser()

    session = Session()

    files = get_word_files(FOLDER_PATH)

    for file_path in files:

        text = read_file(file_path)

        decision = parser.parse(
            text,
            file_path.name
        )

        db_record = DecisionDB(
            decision_number=decision.decision_number,
            decision_date=decision.decision_date,
            case_number=decision.case_number,
            location=decision.location,
            judge=decision.judge,
            source_file=decision.source_file
        )

        session.add(db_record)

        print(
            f"[OK] Обработан файл: "
            f"{file_path.name}"
        )

    session.commit()

    session.close()

    print("Все данные сохранены в БД")


if __name__ == "__main__":
    main()
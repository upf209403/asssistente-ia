from pathlib import Path

BASE_DIR_KNOWLEDGE = Path(__file__).resolve().parent.parent
KNOWLEDGE_PATH = BASE_DIR_KNOWLEDGE / "knowledge"

def load_knowledge(files):

    contents = []

    for file in files:
        path = Path(KNOWLEDGE_PATH)/file

        if path.exists():
            with open(path, "r", encoding="utf-8") as f:

                contents.append(
                    f.read()
                )
    return "\n\n".join(contents)
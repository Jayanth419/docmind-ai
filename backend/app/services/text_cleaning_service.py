import re


class TextCleaningService:

    def clean(self, text: str) -> str:

        if not text:
            return ""

        text = text.replace(
            "\r\n",
            "\n",
        )

        text = text.replace(
            "\r",
            "\n",
        )

        text = re.sub(
            r"[ \t]+",
            " ",
            text,
        )

        text = re.sub(
            r"\n{3,}",
            "\n\n",
            text,
        )

        lines = [
            line.strip()
            for line in text.split("\n")
        ]

        text = "\n".join(lines)

        return text.strip()
import configparser
from typing import Dict


class ConfReaderBase:
    data: Dict
    filepath: str
    config: configparser.ConfigParser

    def __init__(self, path: str) -> None:
        self.filepath = path
        self.data = {}
        self.config = configparser.ConfigParser(
            interpolation=None, allow_no_value=True, delimiters="="
        )

    def _preprocess_multiline_conf(self) -> str:
        """Preprocess .conf file to handle multiline values and avoid duplicates."""
        with open(self.filepath) as f:
            lines = f.readlines()
        lines_iterator = iter(lines)
        processed_lines = []
        for line in lines_iterator:
            # Remove comments and strip whitespace
            line = line.split("#", 1)[0].strip()
            if line:
                while line.endswith("\\"):
                    # Remove the backslash and append the next line
                    line = line[:-1].strip() + " " + next(lines_iterator).strip()
                processed_lines.append(line)

        # Join processed lines into a single string
        return "\n".join(processed_lines)

    def read(self) -> None:
        processed_content = self._preprocess_multiline_conf()
        self.config.read_string(processed_content)

    def to_dict(self) -> Dict:
        return self.data


class ConfReader(ConfReaderBase):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.read()

    def to_dict(self) -> Dict:
        self.data["total"] = len(self.config.sections())
        self.data.update(
            {
                section: dict(self.config.items(section))
                for section in self.config.sections()
            }
        )
        return self.data


class ConfAoB(ConfReaderBase):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.read()

    def get_version(self):
        for section in self.config.sections():
            if "builder_version" in self.config[section]:
                return self.config[section]["builder_version"]


class ConfInputs(ConfReaderBase):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.read()

    def to_dict(self) -> Dict:
        self.data["stanzas"] = self.config.sections()
        self.data["sourcetypes"] = []
        for section in self.config.sections():
            if "sourcetype" in self.config[section]:
                sourcetype_value = self.config[section]["sourcetype"]
                self.data["sourcetypes"].append(sourcetype_value)
        return self.data

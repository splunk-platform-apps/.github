from enum import Enum
from typing import Optional, List, Dict


class KnowledgeObject:
    def __init__(self, context: str, description: str, data: Optional[dict] = {}):
        self.type = context
        self.description = description
        self.data = data

    def __eq__(self, other):
        if isinstance(other, KnowledgeObject):
            return self.type == other.type and self.description == other.description
        return False

    def __hash__(self):
        return hash((self.type, self.description))

    def __repr__(self):
        return f"KnowledgeObject(type={self.type}, description={self.description})"

    def to_dict(self) -> dict:
        return self.__dict__


class Extension:
    def __init__(self, context: str, description: str, built_by: Optional[str] = ""):
        self.type = context
        self.description = description
        self.built_by = built_by

    def __eq__(self, other):
        if isinstance(other, Extension):
            return (
                self.type == other.type
                and self.description == other.description
                and self.built_by == other.built_by
            )
        return False

    def __hash__(self):
        return hash((self.type, self.description, self.built_by))

    def __repr__(self):
        return f"Extension(type={self.type}, description={self.description}, built_by={self.built_by})"

    def to_dict(self) -> dict:
        return self.__dict__


class ReactComponent:
    def __init__(self, name: str, built_by: str):
        self.name = name
        self.built_by = built_by

    def __eq__(self, other):
        if isinstance(other, ReactComponent):
            return self.name == other.name and self.built_by == other.built_by
        return False

    def __hash__(self):
        return hash((self.name, self.built_by))

    def __repr__(self):
        return f"ReactComponent(name={self.name}, built_by={self.built_by})"

    def to_dict(self) -> dict:
        return self.__dict__


class AppClassificationClass(Enum):
    # https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity/abouttheessolution/
    # DA: Correlation searches, saved searches, macros, lookups
    # TA: Lookups, adaptive response actions, tags, eventtypes, props, transforms, indexes, inputs
    # SA: DA + data models + TA (- inputs!)
    APP = "Splunk App"
    SA = "Splunk Support Add-On (SA)"
    DA = "Splunk Domain Add-On (DA)"
    TA = "Splunk Technology Add-On (TA)"
    SUITE = "Splunk App & Add-On"

    @classmethod
    def get_instance(cls, classification_tag: str):
        return AppClassification(
            classification_tag.lower(), cls[classification_tag.upper()].value
        )


class AppBuilderClass(Enum):
    UI = "Splunk UI Toolkit"
    UCC = "UCC Framework"
    AOB = "Add-On Builder (AoB)"
    OTHER = "Other"

    @classmethod
    def get_instance(cls, builder_tag: str):
        return AppBuilder(cls[builder_tag.upper()].value)


class AppClassification:
    def __init__(self, classification_id: str, name: str) -> None:
        self.classification = classification_id
        self.description = name

    def to_dict(self) -> dict:
        return self.__dict__


class AppBuilder:
    name: str
    version: str = ""

    def __init__(self, name: str) -> None:
        self.name = name

    def to_dict(self) -> dict:
        return self.__dict__


class AppSummary:
    classification: AppClassification
    builder: AppBuilder
    notes: str

    def __init__(
        self,
        classification_tag: Optional[str] = None,
        builder_tag: Optional[str] = None,
    ) -> None:
        if classification_tag:
            self.classification = AppClassificationClass.get_instance(
                classification_tag
            )
        if builder_tag:
            self.builder = AppBuilderClass.get_instance(builder_tag)

    def to_dict(self) -> dict:
        result = {}
        for key, value in self.__dict__.items():
            if hasattr(value, "to_dict") and callable(value.to_dict):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result


class ReportBuilder:
    path: str
    id: str
    version: str
    name: str
    u_extensions: List[Extension] = []
    extensions: List[Dict]
    u_knowledge_objects: List[KnowledgeObject] = []
    knowledge_objects: List[Dict]
    u_components: List[ReactComponent] = []
    components: List[Dict]
    summary: AppSummary

    def __init__(self, path: str) -> None:
        self.path = path
        self.extensions = []
        self.knowledge_objects = []
        self.components = []
        self.summary = AppSummary()

    def add_extension(self, extension: Extension) -> None:
        if extension not in self.u_extensions:
            self.extensions.append(extension.to_dict())
            self.u_extensions.append(extension)

    def add_ko(self, ko: KnowledgeObject) -> None:
        if ko not in self.u_knowledge_objects:
            self.knowledge_objects.append(ko.to_dict())
            self.u_knowledge_objects.append(ko)

    def add_component(self, component: ReactComponent) -> None:
        if component not in self.u_components:
            self.components.append(component.to_dict())
            self.u_components.append(component)

    def set_classification(self, classification_tag: str) -> None:
        if not self.summary:
            self.summary = AppSummary(classification_tag)

        if not hasattr(self.summary, "classification"):
            setattr(
                self.summary,
                "classification",
                AppClassificationClass.get_instance(classification_tag),
            )

        if self.summary.classification.classification != classification_tag:
            setattr(
                self.summary,
                "classification",
                AppClassificationClass.get_instance("suite"),
            )
            setattr(
                self.summary,
                "notes",
                "Apps and Add-Ons Knowledge Objects found. Please consider splitting into app and add-on",
            )
        # else current == new -> nothing to do

    def set_builder(self, builder_tag: str, version: Optional[str] = None) -> None:
        # Check whether already set
        if not hasattr(self.summary, "builder"):
            setattr(self.summary, "builder", AppBuilderClass.get_instance(builder_tag))

        if version is not None:
            setattr(self.summary.builder, "version", version)

    def to_dict(self) -> dict:
        result = {}
        exclude_fields = {"u_extensions", "u_knowledge_objects", "u_components"}
        for key, value in self.__dict__.items():
            if key in exclude_fields:
                continue  # Skip this attribute
            if hasattr(value, "to_dict") and callable(value.to_dict):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result

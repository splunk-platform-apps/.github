#!/usr/bin/env python3
import os
import json
from helpers.conf_parsers import *
from helpers.models import *

# -TA
# - Modular input / alert
#   - UCC Framework / AoB
#   - alert-actions.conf / restmap.conf / bin folder has scripts
#   - inputs.conf / restmap.conf / bin folder has scripts
# - Csc
#   - searchbnf.conf
# - Field extractions / Normalizations / Data Collection
#   - props.conf / transforms.conf / inputs.conf
#   - NO savedsearches.conf / views folder
#
# - App (dashboard, lookups, saved searches, etc)
# - Search & Reporting
#   - default/data/ui/views has dashboards
#   - savedsearches.conf
#   - lookups folder
# - MLTK
#   - models.conf / lookups folder has data / bin folder may have scripts
# - Custom Viz
#   - appserver/static/visualizations have js files


def find(report, filename, filepath=None):
    """Find a file in project"""
    for root, dirs, files in os.walk(getattr(report, "path")):
        if filepath is not None:
            if filepath in root and filename in files:
                return os.path.join(root, filename)
        if filename in files:
            # If the file is found, return the full path
            return os.path.join(root, filename)
    return None


def set_general_info(report):
    """Read general info from app.manifest or app.conf"""
    file_path = find(report, "app.manifest")
    if file_path is not None and os.path.exists(file_path):
        try:
            with open(file_path) as file:
                data = json.load(file)

            setattr(report, "id", data["info"]["id"]["name"])
            setattr(report, "version", data["info"]["id"]["version"])
            setattr(report, "name", data["info"]["title"])
        except FileNotFoundError:
            print(f"Error: The file was not found.")
        except json.JSONDecodeError:
            print(f"Error: The file is not a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        file_path = find(report, "app.conf", "/src/main/resources/splunk/default")
        if file_path is not None:
            data = ConfReader(file_path).to_dict()
            setattr(report, "id", data["ui"]["label"])
            setattr(report, "version", data["launcher"]["version"])
            setattr(report, "name", data["launcher"]["description"])


def get_builder(report, globalconfig_meta=None):
    """Get the builder used for building the TA"""
    ret_val = {"name": "other", "version": "unknown"}
    if globalconfig_meta is not None:
        file_path = find(report, "addon_builder.conf")
        if file_path is not None:
            ret_val["name"] = "aob"
            ret_val["version"] = ConfAoB(file_path).get_version()
        if "_uccVersion" in globalconfig_meta:
            ret_val["name"] = "ucc"
            ret_val["version"] = globalconfig_meta["_uccVersion"]
    return ret_val


def detect_splunk_app_type(app_dir, report):
    """Find out details on the project"""
    # Set variables
    globalconfig_path = find(report, "globalConfig.json")

    # Check for each type based on typical files and structure
    for root, dirs, files in os.walk(app_dir):
        # print(f"{root} {dirs} {files}")

        # Check for Search & Reporting App indicators, but exclude inputs.xml
        if "default/data/ui/views" in root:
            xml_files = [
                f
                for f in files
                if f.endswith(".xml") and f not in ["inputs.xml", "configuration.xml"]
            ]
            if xml_files:
                report.add_ko(
                    KnowledgeObject("search_and_reporting", "Dashboards & Views")
                )
                report.set_classification("app")

        # Check for Splunk UI indicators
        if "packages" in root:
            if "webapp/pages/start" in root:
                report.set_classification("app")
                report.set_builder("ui")
            if "src" in root and "main" not in root:
                jsx_files = [f for f in files if f.endswith(".jsx")]
                if jsx_files:
                    path_split = root.split(os.sep)
                    index = path_split.index("packages") + 1
                    report.add_component(
                        ReactComponent(f"{path_split[index]}", "Splunk UI")
                    )
            # TODO test this when app comes with for example custom handlers
            # restmap.conf / web.conf / files in bin

        if "savedsearches.conf" in files:
            report.add_ko(
                KnowledgeObject(
                    "search_and_reporting",
                    "Saved Searches & Correlation Searches",
                    ConfReader(os.path.join(root, "savedsearches.conf")).to_dict(),
                )
            )

        if "default/data/models" in root and "datamodels.conf" in files:
            report.add_ko(KnowledgeObject("search_and_reporting", "Data Models"))

        if "macros.conf" in files:
            report.add_ko(KnowledgeObject("search_and_reporting", "Macros"))

        if "appserver/static/visualizations" in root:
            report.add_extension(
                Extension("search_and_reporting", "Custom Visualization")
            )
            report.set_classification("app")

        if "models.conf" in files or "notebooks" in dirs:
            report.add_ko(
                KnowledgeObject(
                    "search_and_reporting", "Machine Learning Toolkit (MLTK)"
                )
            )
            report.set_classification("app")

        if "lookups" in root:
            csv_files = [f for f in files if f.endswith(".csv")]
            if csv_files:
                report.add_ko(KnowledgeObject("data_parsing", "Lookups"))

        if any(f in files for f in ["props.conf", "transforms.conf", "inputs.conf"]):
            # May be expanded by reading files and extracting data
            report.add_ko(
                KnowledgeObject("data_parsing", "Data Parsing & Fields Extraction")
            )
            report.set_classification("ta")

        if any(f in files for f in ["eventtypes.conf", "tags.conf"]):
            # May be expanded by reading files and extracting data
            report.add_ko(KnowledgeObject("data_parsing", "Event Types & Tags"))

        if "bin" in root:
            # Look for Python or Shell scripts in the bin folder
            custom_files = [f for f in files if f.endswith(".py") or f.endswith(".sh")]
            if custom_files:
                # Check for commands.conf
                if find(report, "commands.conf") is not None:
                    report.add_ko(
                        KnowledgeObject("data_parsing", "Custom Search Command")
                    )
                    report.set_classification("ta")

                builder = get_builder(report)

                # Check for other Add-on indicators
                if globalconfig_path is not None:
                    # Could be built using UCC or AoB
                    try:
                        with open(globalconfig_path) as file:
                            data = json.load(file)

                        builder = get_builder(report, data["meta"])

                        if "inputs" in data["pages"]:
                            report.add_extension(
                                Extension(
                                    "data_parsing",
                                    "Modular Input",
                                    getattr(
                                        AppBuilderClass.get_instance(builder["name"]),
                                        "name",
                                    ),
                                )
                            )
                            report.set_classification("ta")
                        if "alerts" in data and len(data["alerts"] > 0):
                            if any(
                                "adaptiveResponse" in alert for alert in data["alerts"]
                            ):
                                report.add_extension(
                                    Extension(
                                        "data_parsing",
                                        "Adaptive Response Action",
                                        getattr(
                                            AppBuilderClass.get_instance(
                                                builder["name"]
                                            ),
                                            "name",
                                        ),
                                    )
                                )
                            else:
                                report.add_extension(
                                    Extension(
                                        "data_parsing",
                                        "Alert Action",
                                        getattr(
                                            AppBuilderClass.get_instance(
                                                builder["name"]
                                            ),
                                            "name",
                                        ),
                                    )
                                )
                            report.set_classification("ta")
                    except FileNotFoundError:
                        print(f"Error: The file was not found.")
                    except json.JSONDecodeError:
                        print(f"Error: The file is not a valid JSON file.")
                    except Exception as e:
                        print(f"An unexpected error occurred: {e}")

                elif "alert_actions.conf" in files:
                    report.add_extension(
                        Extension(
                            "data_parsing",
                            "Alert Action or Adaptive Response Action",
                            getattr(
                                AppBuilderClass.get_instance(builder["name"]), "name"
                            ),
                        )
                    )
                    report.set_classification("ta")

                elif "inputs.conf" in files:
                    report.add_extension(
                        Extension(
                            "data_parsing",
                            "Modular Input",
                            getattr(
                                AppBuilderClass.get_instance(builder["name"]), "name"
                            ),
                        )
                    )
                    report.set_classification("ta")

                report.set_builder(builder["name"], builder["version"])

    # Fallback case: only KOs found
    if not report.summary.classification and len(report.u_knowledge_objects) > 0:
        report.set_classification("app")

    return report.to_dict()


def generate_report_json(output_file="splunk_app_type_report.json"):
    # Detect the app type(s)
    app_dir = os.environ.get("APP_DIRECTORY")

    report = ReportBuilder(app_dir)
    set_general_info(report)
    detection_report = detect_splunk_app_type(app_dir, report)

    # Write the report to a JSON file
    with open(output_file, "w") as f:
        json.dump(detection_report, f, indent=4)

    print(f"Detection report saved to {output_file}")

    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        print(f"reportpath={output_file}", file=fh)


if __name__ == "__main__":
    generate_report_json()

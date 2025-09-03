# Action for Splunk App Detector
This action aims reading the content of your source files and providing a report on the detected knowledge objects and extensions.

:construction: **This is a WIP and content may change** :construction:

## Usage
Use the action within your own Github worflows as shown below
```yaml
- name: Run detector
    id: detector
    uses: ./.github/actions/splunk-apps-detector
    with:
        - app-directory: /path/to/source
```
### Inputs
* `app-directory` is optional. Default value: `./package`

### Outputs
* `report-path` gives the path to the generated JSON named `splunk_app_type_report.json`

The file is structured as follows:

* `path` will report the path to the app source code
* `id`, `version` and `name` will report app ID, version and name
* `knowledge_objects` will contain a list of found knowledge objects. Each object could be extended to add some data coming from parsing of specific `.conf` files
* `extensions` will contain a list of found extensions (i.e. Modular Alerts, Alert Actions or Adaptive Response Actions, Modular Visualizations and Modular Inputs)
* `components` will contain a list of React components (relevant for Splunk Apps built via Splunk UI toolkit)
* `summary` will contain final detection recap info

Report example:

```json
{
    "path": "/path/to/source",
    "id": "TA-demo",
    "version": "1.0.0",
    "name": "SW Demo",
    "knowledge_objects": [
        {
            "type": "data_parsing",
            "description": "Data Parsing & Fields Extraction"
        }
    ],
    "extensions": [
        {
            "type": "data_parsing",
            "description": "Modular Input",
            "built_by": "Add-On Builder (AoB)"
        }
    ],
    "components": [],
    "summary": {
        "classification": "ta",
        "description": "Splunk Technology Add-On (TA)",
        "builder": {
            "name": "Add-On Builder (AoB)",
            "version": "4.2.0"
        },
        "notes": ""
    }
}
```
Supported values for `type` are: `data_parsing` and `search_and_reporting`


## References
* [Splunk Apps and Add-Ons](https://www.splunk.com/en_us/blog/tips-and-tricks/what-are-splunk-apps-and-add-ons.html)
* [Splunk Apps VS Add-Ons](https://community.splunk.com/t5/Getting-Data-In/What-is-the-difference-between-apps-add-ons-and-TAs-and-where/m-p/253506)
* [Enterprise Security Apps & Add-Ons Definitions](https://dev.splunk.com/enterprise/docs/devtools/enterprisesecurity/abouttheessolution/)
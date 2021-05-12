
import json
from typing import Dict, Union


class Report:
    id_key = 'id'
    name_key = 'name'
    web_url_key = 'webUrl'
    embed_url_key = 'embedUrl'
    dataset_id_key = 'datasetId'
    target_workspace_id_key = 'targetWorkspaceId'
    target_model_id_key = 'targetModelId'

    def __init__(self, report_id, name, web_url, embed_url, dataset_id):
        self.id = report_id
        self.name = name
        self.web_url = web_url
        self.embed_url = embed_url
        self.dataset_id = dataset_id

    @classmethod
    def from_dict(cls, dictionary):
        """
        Creates a report from a dictionary
        :param dictionary: The dictionary to create a report from
        :return: The created dictionary
        """
        # id is required
        if cls.id_key in dictionary:
            report_id = str(dictionary[cls.id_key])
            # id cannot be whitespace
            if report_id.isspace():
                raise RuntimeError(f'Report dict has empty {cls.id_key} key value')
        else:
            raise RuntimeError(f'Report dict has no {cls.id_key} key')

        # name is required
        if cls.name_key in dictionary:
            report_name = str(dictionary[cls.name_key])
            # name cannot be whitespace
            if report_name.isspace():
                raise RuntimeError(f'Report dict has empty {cls.name_key} key value')
        else:
            raise RuntimeError(f'Report dict has no {cls.name_key} key')

        # web url is optional
        if cls.web_url_key in dictionary:
            web_url = str(dictionary[cls.web_url_key])
        else:
            web_url = None

        # embed url is optional
        if cls.embed_url_key in dictionary:
            embed_url = str(dictionary[cls.embed_url_key])
        else:
            embed_url = None

        # dataset id is optional
        dataset_id = dictionary.get(cls.dataset_id_key)

        return Report(report_id, report_name, web_url, embed_url, dataset_id)

    def __repr__(self):
        return f'<Report {str(self.__dict__)}>'


class SourceReport:
    source_report_id_key = 'sourceReportId'
    source_workspace_id_key = 'sourceWorkspaceId'

    def __init__(
        self,
        source_report_id: str,
        source_workspace_id: str
    ):
        """Creates a SourceReport object

        :param source_report_id: the source report id
        :param source_workspace_id: the source workspace id
        """
        self.source_report_id = source_report_id
        self.source_workspace_id = source_workspace_id

    def as_dict(self) -> Dict[str, str]:
        return {
            self.source_report_id_key: self.source_report_id,
            self.source_workspace_id_key: self.source_workspace_id
        }

    def __repr__(self) -> str:
        return f'<SourceReport report_id={self.source_report_id} workspace_id={self.source_workspace_id}>'


class UpdateReportContentRequest:
    # The source type for the content update.
    source_type = "ExistingReport"  # Use an existing report as a source for updating the content of a target report.
    source_type_key = "sourceType"
    source_report_key = "sourceReport"

    def __init__(
        self,
        source_report: SourceReport
    ):
        """Creates an UpdateReportContentRequest

        :param source_report: Source from existing report
        """
        self.source_report = source_report

    def as_dict(self) -> Dict[str, Union[Dict[str, str], str]]:
        return {
            self.source_report_key: self.source_report.as_dict(),
            self.source_type_key: self.source_type
        }

    def __repr__(self):
        return f'<UpdateReportContentRequest sourceReport={self.source_report} sourceType={self.source_type}>'


class ReportEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            Report.id_key: o.id,
            Report.name_key: o.name,
            Report.web_url_key: o.web_url,
            Report.embed_url_key: o.embed_url,
            Report.dataset_id_key: o.dataset_id
        }

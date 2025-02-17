import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.openstack_cloud_endpoint import OpenstackCloudEndpoint
from steps.api.openstack_project_endpoint import OpenstackProjectEndpoint


class OpenstackEndpoint(BaseEndpoint):
    """
    Represents the OpenStack API endpoint.
    """

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.cloud = OpenstackCloudEndpoint(session, admin_session)
        self.project = OpenstackProjectEndpoint(session, admin_session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/openstack{suffix}"

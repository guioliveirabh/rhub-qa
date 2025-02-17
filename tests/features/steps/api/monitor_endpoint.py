import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.monitor_bm_endpoint import MonitorBMEndpoint
from steps.api.monitor_lab_endpoints import MonitorLabEndpoint
from steps.api.monitor_vm_endpoint import MonitorVMEndpoint


class MonitorEndpoint(BaseEndpoint):
    """
    Represents the /monitor API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.bm = MonitorBMEndpoint(session, admin_session)
        self.lab = MonitorLabEndpoint(session, admin_session)
        self.vm = MonitorVMEndpoint(session, admin_session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/monitor{suffix}"

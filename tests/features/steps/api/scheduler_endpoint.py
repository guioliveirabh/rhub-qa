import requests

from steps.api.base_endpoint import BaseEndpoint
from steps.api.scheduler_cron_endpoint import SchedulerCronEndpoint


class SchedulerEndpoint(BaseEndpoint):
    """
    Represents the /scheduler API endpoint.
    """

    UNVERIFIABLE_ITEMS = {}

    def __init__(self, session: requests.Session, admin_session: requests.Session):
        super().__init__(session, admin_session)

        self.cron = SchedulerCronEndpoint(session, admin_session)

    def url(self, suffix: str = '') -> str:
        return f"{self.base_url}/scheduler{suffix}"

import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from behave import fixture


# https://jenisys.github.io/behave.example/


class ResourceHubCLI:
    API_BASE_URL = 'http://localhost:8081/v0'
    API_USER = 'testuser1'
    API_PASS = 'testuser1'

    # TODO: API needs to be on the same version as the CLI code being tested
    PIP_CLONE_URL = 'git@github.com:resource-hub-dev/rhub-cli.git'

    def __init__(self, virtual_environment_path: Path):
        self.entrypoint = str(virtual_environment_path / 'bin/rhub-cli')
        self.base_command = [
            self.entrypoint,
            '--base-url', self.API_BASE_URL,
            '--user', self.API_USER,
            '--password', self.API_PASS,
        ]
        self.last_output = ''

    def run(self, cli_args: list[str]):
        self.last_output = ''
        command = self.base_command + cli_args
        process_status = subprocess.run(
            command,
            check=True,
            capture_output=True,
        )
        self.last_output = process_status.stdout


@fixture
def resource_hub_cli(context):
    with TemporaryDirectory() as temp_directory_str:
        temp_directory_path = Path(temp_directory_str)

        # create temporary python virtual environment
        subprocess.run(
            [sys.executable, '-m', 'venv', temp_directory_str],
            check=True,
        )

        # install RHub CLI on the created virtual environment
        subprocess.run(
            f"{temp_directory_path / 'bin/activate'} ; pip install {ResourceHubCLI.PIP_CLONE_URL}",
            check=True,
            shell=True,
        )

        context.cli = ResourceHubCLI(temp_directory_path)
        yield context.cli

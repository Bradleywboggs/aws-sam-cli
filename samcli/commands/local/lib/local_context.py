from samcli.cli.context import Context
import click


class LocalContext(Context):
    def __init__(self):
        super().__init__()
        self._aws_account_id = None

    @property
    def aws_account_id(self):
        return self._aws_account_id

    @aws_account_id.setter
    def aws_account_id(self, value):
        self._aws_account_id = value
        self._refresh_session()


pass_context = click.make_pass_decorator(LocalContext)

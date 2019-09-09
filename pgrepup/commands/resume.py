from clint.textui import indent
from ..helpers.replication import *
from ..helpers.docopt_dispatch import dispatch
from ..helpers.ui import *
from ..helpers.database import *


@dispatch.on('resume')
def resume(**kwargs):

    # Shortcut to ask master password before output Configuration message
    decrypt(config().get('Source', 'password'))

    output_cli_message("Resume replication and upgrade", color='cyan')
    puts("")
    databases = get_cluster_databases(connect('Destination'))
    with indent(4, quote=' >'):
        for d in databases:
            output_cli_message(d)
            print(output_cli_result(resume_subscription(d), 4))

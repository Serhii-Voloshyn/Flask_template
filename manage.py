import argparse
import sys
import logging

from service_api.app import app


logger = logging.getLogger(__name__)


def parse_args(args):
    """This function parses parameters before starting service."""

    parser = argparse.ArgumentParser(description="Sanic rest api skeleton", add_help=False)
    parser.add_argument("--help", action="help", help="show this help message and exit")

    subparsers = parser.add_subparsers(dest="command")

    sparser = subparsers.add_parser(runserver.__name__, add_help=False, help="Discover all clients dbs")
    sparser.add_argument("-h", "--host", dest="host", default="0.0.0.0", type=str, help="Host address")
    sparser.add_argument("-p", "--port", dest="port", default=5000, type=int, help="Host post")

    return parser.parse_args(args=args)


def runserver(host, port):
    """This function setup params and run server.

    Args:
        host (str): Host where server will be running.
        port (str): Port where server will be running.

    """

    app.run(host=host, port=port)


def main(args=None):
    """This function is responsible for running the required functionality, depending on the arguments provided."""
    parsed_args = parse_args(args or sys.argv[1:])

    if parsed_args.command == runserver.__name__:
        runserver(parsed_args.host, parsed_args.port)
    else:
        logger.info("Service stopped.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.critical(
            "Unexpected exception occurred. Service is going to shutdown. Error message: {}".format(e),
            extra={"error_message": e},
        )
        exit(1)
    finally:
        logger.info("Service stopped.")

import argparse
import os
from typing import Dict, Callable
import sys
from typing import Tuple, Union
from logging import Logger

list_of_tasks = ["locate", "version"]


def main(
    main_filename: str,
    NAME: str,
    VERSION: str,
    DESCRIPTION: str,
    ICON: str,
    tasks: Dict[str, Callable] = {},
) -> Tuple[bool, str]:
    parser = argparse.ArgumentParser(NAME, description=f"{NAME}-{VERSION}")
    parser.add_argument(
        "task",
        type=str,
        help="|".join(list_of_tasks),
    )
    parser.add_argument(
        "--show_description",
        type=int,
        default=0,
        help="0|1",
    )
    parser.add_argument(
        "--show_icon",
        type=int,
        default=0,
        help="0|1",
    )
    args = parser.parse_args()

    success = args.task in list_of_tasks
    if args.task in tasks:
        success = tasks[args.task](args)
    elif args.task == "locate":
        print(os.path.dirname(os.path.abspath(main_filename)))
    elif args.task == "version":
        print(
            "{}{}-{}{}".format(
                f"{ICON} " if args.show_icon else "",
                NAME,
                VERSION,
                "\\n{}".format(DESCRIPTION) if args.show_description else "",
            )
        )
    else:
        return False, f"-{NAME}: {args.task}: command not found."

    return success, ("" if success else f"-{NAME}: {args.task}: failed.")


def sys_exit(
    logger: Logger,
    NAME: str,
    task: str,
    success: Union[bool, None],
    log: bool = True,
):
    if log:
        if success is None:
            logger.error(f"-{NAME}: {task}: command not found.")
        elif not success:
            logger.error(f"-{NAME}: {task}: failed.")

    if success is True:
        sys.exit(0)

    sys.exit(1)

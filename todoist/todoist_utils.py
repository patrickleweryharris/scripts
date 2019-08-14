#!/usr/local/bin/python3
"""
Utility functions for my todoist scripts
"""
import os
import argparse
from todoist.api import TodoistAPI


def create_parser():
    """ Create argparse object for this CLI """
    parser = argparse.ArgumentParser(
        description="Add an item to a specified todoist project")

    parser.add_argument("item", metavar="ITEM",
                        help="Name of item to add")
    parser.add_argument("project", metavar="PROJECT",
                        help="Name of project to add to")
    parser.add_argument("--label", metavar="LABEL",
                        default=False,
                        help="Label to add to project")
    parser.add_argument("--date_string", metavar="DATE",
                        default="next year",
                        help="Due date for project")
    return parser


def get_token():
    """ Return API token """
    token = os.getenv('TODOIST_API_TOKEN')
    return token


def get_id(name, component):
    """ Get the id for a specific name in a component"""
    api = TodoistAPI(get_token())
    api.sync()
    items = api.state[component]
    for item in items:
        if item['name'].lower() == name.lower():
            return item['id']

    # if we reach this point, the specified project does not exist
    raise RuntimeError('{} does not exist in {}!'.format(name, component))


def get_project_id(name):
    return get_id(name, 'projects')


def get_label_id(name):
    return get_id(name, 'labels')


def add_to_project(project, name, label=False, date=False):
    """ Add an item to a project """
    token = get_token()
    api = TodoistAPI(token)

    # Hazel will give a full path as the task name, which we don't want
    basename = name
    if os.path.exists(name):
        basename = os.path.splitext(os.path.basename(name))[0]

    due_date = date
    if not date:
        due_date = 'next year'
    if label:
        api.items.add(basename, project_id=get_project_id(project),
                      labels=[get_label_id(label)],
                      date_string=due_date)
    else:
        api.items.add(basename, project_id=get_project_id(project),
                      date_string=due_date)

    api.commit()


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    add_to_project(args.project, args.item, args.label, args.date_string)

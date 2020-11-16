#!/usr/bin/env python3

import json
import logging
import yaml

from pathlib import Path


def validate_schema(self, rule_file):
    """[summary]

    Args:
        rule_file ([type]): [description]

    Returns:
        [type]: [description]
    """
    if rule_file.is_file() and rule_file.exists() and rule_file.suffix == ".yml":
        outcome = "valid_yaml"

    elif rule_file.is_file() and rule_file.exists() and rule_file.suffix == ".json":
        outcome = "valid_json"
    else:
        outcome = "invalid"

    return outcome

def get_json(content, content_type):
    """Convert YAML formatted content to JSON

    Args:
        content (string): Name of file to convert
        content_type ([type]): Type of content to convert, i.e. LiveQuery,
                                policy rule

    Returns:
        string: JSON formatted data
    """

    content_file = Path.cwd().joinpath('content', content_type, content)

    json_conversion = json.dumps(yaml.safe_load(open(content_file, "r")), sort_keys=False, indent=4)

    return json_conversion

def get_yaml(rule_file):
    """[summary]

    Args:
        rule_file ([type]): [description]
    """
    return



def run(rule_file, content_type):
    """[summary]

    Args:
        rule_file ([type]): [description]
        content_type ([type]): [description]
    """
    #validate_schema(rule_file)
    return

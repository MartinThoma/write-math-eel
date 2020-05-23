#!/usr/bin/env python

"""Start a GUI to classify symbols."""

# Core Library modules
import json
import logging

# Third party modules
import eel
import hwrt
from hwrt import classify

logger = logging.getLogger(__name__)


def get_json_result(results, n=10):
    """Return the top `n` results as a JSON list.
    >>> results = [{'probability': 0.65,
    ...             'whatever': 'bar'},
    ...            {'probability': 0.21,
    ...             'whatever': 'bar'},
    ...            {'probability': 0.05,
    ...             'whatever': 'bar'},]
    >>> get_json_result(results, n=10)
    [{'\\alpha': 0.65}, {'\\propto': 0.25}, {'\\varpropto': 0.0512}]
    """
    s = []
    last = -1
    for res in results[: min(len(results), n)]:
        if res["probability"] < last * 0.5 and res["probability"] < 0.05:
            break
        if res["probability"] < 0.01:
            break
        s.append(res)
        last = res["probability"]
    return json.dumps(s)


@eel.expose
def worker(strokelist):
    """Classify the drawn symbol."""
    results = classify.classify_segmented_recording(json.dumps(strokelist))
    return get_json_result(results, n=10)


if __name__ == "__main__":
    eel.init("web")
    eel.start("canvas.html", jinja_templates="templates")

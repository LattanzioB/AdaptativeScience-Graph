#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pyshacl import validate
from rdflib import Graph


def parse_turtle(path: Path) -> Graph:
    graph = Graph()
    graph.parse(path, format="turtle")
    return graph


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Turtle data with SHACL.")
    parser.add_argument("--data", required=True, type=Path, help="Data graph in Turtle format.")
    parser.add_argument("--shapes", required=True, type=Path, help="SHACL shapes graph in Turtle format.")
    parser.add_argument("--inference", default="rdfs", choices=["none", "rdfs", "owlrl", "both"])
    args = parser.parse_args()

    data_graph = parse_turtle(args.data)
    shapes_graph = parse_turtle(args.shapes)

    conforms, report_graph, report_text = validate(
        data_graph,
        shacl_graph=shapes_graph,
        inference=args.inference,
        advanced=True,
        meta_shacl=False,
        debug=False,
    )

    print(report_text)
    return 0 if conforms else 1


if __name__ == "__main__":
    sys.exit(main())

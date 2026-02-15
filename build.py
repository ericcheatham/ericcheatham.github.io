#!/usr/bin/env python3
"""Build the portfolio site by rendering Jinja2 templates with YAML data."""

import shutil
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
BUILD_DIR = ROOT / "_site"
DATA_DIR = ROOT / "_data"
ASSETS_DIR = ROOT / "assets"
TEMPLATES_DIR = ROOT / "templates"


def load_data() -> dict:
    """Load all YAML files from _data/ into a dict keyed by filename."""
    data = {}
    for f in DATA_DIR.glob("*.yml"):
        with open(f) as fh:
            data[f.stem] = yaml.safe_load(fh)
    return data


def build():
    # Clean build directory
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir()

    # Copy static assets
    shutil.copytree(ASSETS_DIR, BUILD_DIR / "assets")

    # Load data and render template
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
    template = env.get_template("index.html")

    data = load_data()
    html = template.render(
        year=datetime.now().year,
        experience=data.get("experience", []),
        skills=data.get("skills", []),
    )

    (BUILD_DIR / "index.html").write_text(html)
    print(f"Built site to {BUILD_DIR}")


if __name__ == "__main__":
    build()

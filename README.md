# ericcheatham.github.io

Personal portfolio site for Eric Cheatham. Built with Python (Jinja2 + PyYAML) and deployed to GitHub Pages via GitHub Actions.

## Project Structure

```
.
├── build.py              # Renders templates with data, outputs to _site/
├── templates/
│   └── index.html        # Jinja2 template for the site
├── _data/
│   ├── experience.yml    # Work history
│   └── skills.yml        # Skills list
├── assets/
│   └── css/
│       └── style.css     # Stylesheet
├── requirements.txt      # Python dependencies
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions build + deploy
```

## Local Development

Requires Python 3.9+.

```bash
# Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Build the site
python build.py

# Open it
open _site/index.html
```

The build script reads YAML data from `_data/`, renders the Jinja2 template, and writes the output to `_site/`.

## Updating Content

- **Experience**: Edit `_data/experience.yml`
- **Skills**: Edit `_data/skills.yml`
- **Everything else** (about text, hero, contact links): Edit `templates/index.html`
- **Styles**: Edit `assets/css/style.css`

## Deployment

Pushes to `main` trigger a GitHub Actions workflow that builds the site and deploys to GitHub Pages. Make sure your repo's Pages settings are set to source: **GitHub Actions**.

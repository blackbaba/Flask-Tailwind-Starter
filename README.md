# Flask + TailwindCSS Starter Template

## Key Features
- Basic Flask app scaffolding
- TailwindCSS setup using npm (with purge implemented for Production)

## How to use
Setup and activate a virtual python environment before proceeding.

Clone the repository onto your local computer and run:

1. `pip install -r requirements.txt` to install flask packages
2. `npm install` to install npm packages from `package.json`
3. `npm run develop:css` to build Tailwind for development (no purge) and start Flask application by running `python run.py`.
4. When ready for production run  `npm run build:css` to prepare a purged CSS build for production

Enjoy!
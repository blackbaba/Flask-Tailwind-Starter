# Flask + TailwindCSS Starter Template with PostCSS+PurgeCSS
---

## How to use
Clone the repository onto your local computer and:

1. `pip install -r requirements.txt` to install flask packages (assuming you have already a virtual python environment setup)
2. `npm install` to install npm packages
3. Start Flask application by running `python run.py`
4. In a separate terminal, run `npm run watch` for Development or `npm run build:css` to build Tailwind for production (static/dist/css/main.css is the final build)

**Note**
Purge setting is controlled manually - set `enabled: true` for purge configuration in tailwind.config.js to enable purge (usually before deploy to production). 
Alternatively, it may be possible to enable auto purge in PROD using NODE_ENV variable. 
This template is setup using the manual option.

Enjoy!
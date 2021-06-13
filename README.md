# Flask + TailwindCSS Starter Template
**Now updated with the [Tailwind JIT compiler mode](https://tailwindcss.com/docs/just-in-time-mode#enabling-jit-mode)**

With the (new highly efficient) Tailwind JIT compiler, purging of unused styles takes place both in development and production. 

## Key Features
- Basic Flask app scaffolding
- TailwindCSS setup using npm

## How to use
Setup and activate a virtual python environment before proceeding.

Clone the repository onto your local computer and run:

1. `pip install -r requirements.txt` to install flask packages
2. `npm install` to install npm packages from `package.json`
3. In one terminal run `npm run dev` to run Tailwind in JIT watch mode during development - this will start real time compilation of styles used in your HTML templates
4. In second terminal run `python run.py` to start the Flask development server (debug mode is ON). As you add/remove Tailwind classes in HTML templates, the watcher running in step 3 will automatically regenerate your `app\static\main.css` file which is picked up the flask server running in step 4.
4. When ready for production, kill the Flask development server in step 3 and run  `npm run build:prod` to prepare CSS build ready for production

Enjoy!

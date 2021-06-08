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
3. In one terminal run `npm run dev` to run Tailwind in JIT watch mode during development (or you can run `npm run build:dev` for a one time development build - ideally the watch mode is all you need as it compiles and purges each style change in real time in < 1 second during development)
4. In second terminal run `python run.py` to start the Flask app. As you add/remove Tailwind classes in HTML templates, the watcher running in step 3 will automatically regenerate your `app\static\main.css` file.
4. When ready for production, kill the server in step 3 and run  `npm run build:prod` to prepare CSS build ready for production

Enjoy!

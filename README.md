# Flask + TailwindCSS Starter Template
Now updated with the [Tailwind JIT compiler](https://tailwindcss.com/docs/just-in-time-mode#enabling-jit-mode)

## Key Features
- Basic Flask app scaffolding
- TailwindCSS setup using npm (with purge implemented for Production)

## How to use
Setup and activate a virtual python environment before proceeding.

Clone the repository onto your local computer and run:

1. `pip install -r requirements.txt` to install flask packages
2. `npm install` to install npm packages from `package.json`
3. `npm run dev` to build Tailwind in JIT watch mode for during development or `npm run build:dev` for a one time development build 
4. When ready for production run  `npm run build:prod` to prepare CSS build ready for production

Enjoy!


  // Will start a long-running watch process
    "dev": "TAILWIND_MODE=watch NODE_ENV=development postcss tailwind.css -o ./dist/tailwind.css -w"
    // Will perform a one-off development build
    "build:dev": "TAILWIND_MODE=build NODE_ENV=development postcss tailwind.css -o ./dist/tailwind.css"
    // Will perform a one-off production build
    "build:prod": "TAILWIND_MODE=build NODE_ENV=production postcss tailwind.css -o ./dist/tailwind.css"
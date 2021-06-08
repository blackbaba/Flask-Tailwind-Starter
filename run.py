from app import app

if __name__ == "__main__":
    app.config['ENV']="development"
    app.run(debug=True)

from app import app

if __name__ == "__main__":
    app.config['DEBUG']=1
    app.config['ENV']="development"
    app.run()

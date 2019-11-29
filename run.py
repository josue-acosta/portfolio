from app import app

# run app
if __name__ == '__main__':
    print("Python environment:", app.config["ENV"])
    app.run()
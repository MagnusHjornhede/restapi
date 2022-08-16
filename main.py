from website import create_app

app = create_app()

if __name__ == '__main__':  # Needed to run a flask app
    app.run(debug=True)
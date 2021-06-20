from __init__ import create_app
import background_tasks


app = create_app()
background_tasks.init()


if __name__ == "__main__":
    APP_PORT = app.config["APP_PORT"]
    APP_HOST = app.config["APP_HOST"]

    app.run(debug=False, host=APP_HOST, port=APP_PORT, threaded=True)

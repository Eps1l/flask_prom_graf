from app import app
from flask import Flask
from flask import render_template
from prometheus_flask_exporter import PrometheusMetrics
import time, sys, requests, datetime, threading

metrics = PrometheusMetrics(app)


@app.route('/metrics')
@metrics.do_not_track()
def appp():
    pass

@app.route('/')
def home():
    return render_template('index.html')

def start_runner():
    def everymin():
        while True:
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            req = requests.get("http://192.168.1.247:56733/").status_code

            if req == 200:
                with open('/app/app/logs/healthcheck.log', 'a') as f:
                    print(date,"Hello world page is OK. Status code:",req, file=f)
            else:
                with open('/app/app/logs/healthcheck_error.log', 'a') as f:
                    print(date,"Bad page status is:",req, file=f)
            time.sleep(10)

    print('Started runner')

    threading.Thread(target=everymin, daemon=True).start()

start_runner()

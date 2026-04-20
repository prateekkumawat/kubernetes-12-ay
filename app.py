from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

def check_redis():
    try:
        redis.ping()
        return True
    except Exception:
        app.logger.exception("Redis health check failed")
        return False

@app.route('/health')
def health():
    if check_redis():
        return 'OK\n', 200
    return 'Redis unavailable\n', 503

@app.errorhandler(Exception)
def handle_exception(error):
    app.logger.exception("Unhandled exception")
    return 'Internal Server Error\n', 500

@app.route('/')
def hello():
    redis_ok = check_redis()
    count = redis.incr('hits') if redis_ok else 0
    message = (
        'Redis is connected and the visit count has been updated.'
        if redis_ok else
        'Redis is unavailable. Refresh the page again once Redis is reachable.'
    )
    return render_template(
        'index.html',
        count=count,
        redis_ok=redis_ok,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
# utils/helpers.py

def safe_int(value, default=0):
    try:
        return int(value)
    except:
        return default

def safe_run(fn, *args, **kwargs):
    try:
        return fn(*args, **kwargs)
    except Exception as e:
        return {"error": str(e)}

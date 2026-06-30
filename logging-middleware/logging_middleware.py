import requests
log_api = "http://4.224.186.213/evaluation-service/logs"
def Log(stack, level, package, message):
    payload = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }
    try:
        response = requests.post(log_api, json=payload, timeout=5)
        return response.status_code
    except Exception as e:
        print("Logging Error:", e)
        return None


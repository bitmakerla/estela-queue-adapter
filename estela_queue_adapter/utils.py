from datetime import date, datetime

# libraries to be silenced by the entrypoint logger
queue_noisy_libraries = ["kafka"]


def get_bootstrap_servers(listeners, port):
    return [f"{listener}:{port}" for listener in listeners.split(",")]


def json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if hasattr(obj, "__str__"):
        return str(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

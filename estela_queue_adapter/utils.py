# libraries to be silenced by the entrypoint logger
queue_noisy_libraries = ["kafka"]


def get_bootstrap_servers(listeners, port):
    return [f"{listener}:{port}" for listener in listeners.split(",")]

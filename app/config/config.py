

class SentinelConfig:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SentinelConfig, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        # initialize config only once
        if not hasattr(self, "_initialized"):
            # Put your config setup here
            self.value = "default"
            self._initialized = True

sentinel_config = SentinelConfig()

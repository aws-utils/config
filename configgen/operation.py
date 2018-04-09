from troposphere import awslambda

class Operation:
    def __init__(self, config=None):
        for k, v in config.items():
            setattr(self, k, v)

    

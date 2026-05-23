class LLMBridge:
    def __init__(self):
        self.provider = 'mock'

    def execute_task(self, task, site_name=None):
        return {
            'ok': True,
            'task': task,
            'site': site_name,
            'result': 'This is a placeholder response from v2.1.'
        }

    def chat(self, message, site_name=None):
        return {
            'ok': True,
            'message': message,
            'site': site_name,
            'response': 'Welcome to EN MOSTAFA AI AGENT v2.1!'
        }

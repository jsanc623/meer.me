class Website(object):
    def __init__(self, db, queue, config):
        self.db = db
        self.queue = queue
        self.config = config

    def home(self):
        return 'meer.me'

    def about(self):
        return 'about'
class Api(object):
    def __init__(self, db, queue, config, user):
        self.db = db
        self.queue = queue
        self.config = config
        self.user_model = user

    def user(self, user_id=None):
        user_id = user_id if user_id is not None else self.user_model.id

        return "Profile for user_id %s" % user_id

    def feed(self, f_type='public'):
        """ Get either a public or private feed with multiple posts
        :param f_type:
        :return:
        """
        if f_type not in ['public', 'private']:
            raise ValueError('Type of feed not determined')

        return str(f_type) + " feed for user " + str(self.user_model.id)

    def friends(self):
        return "Friends of user_id %s" % self.user_model.id

    def messages(self, message_id=None):
        return "Viewing message_id %s" % message_id

    def post(self, post_id):
        return "Viewing post_id %s" % post_id
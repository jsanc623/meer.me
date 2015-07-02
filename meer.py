from flask import Flask

from app.api import Api
from app.website import Website
from app.models.user import User
from app.lib.config import Config
from app.lib.database.db import DB
from app.lib.queue.queue import Queue

if __name__ == '__main__':
    app = Flask(__name__)

    # load libs
    Db = DB()
    Queue = Queue()
    Config = Config()
    User = User()

    User.id = "00000000001"

    # "controllers"
    Website = Website(Db, Queue, Config)
    Api = Api(Db, Queue, Config, User)

    # Website rules
    app.add_url_rule('/', 'home', Website.home, methods=['GET'])
    app.add_url_rule('/about', 'about', Website.about, methods=['GET'])

    # API rules
    # handle profile interaction identified by user_id, defaulting to the id of the active user
    app.add_url_rule('/v1/user/', 'user', Api.user, methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.add_url_rule('/v1/user/<int:user_id>', 'user', Api.user, methods=['GET', 'POST', 'PUT', 'DELETE'])

    # handle feed interaction where f_type is either 'public' or 'private' (defaults: 'public')
    app.add_url_rule('/v1/feed/', 'feed', Api.feed, methods=['GET', 'POST', 'PUT', 'DELETE'])
    app.add_url_rule('/v1/feed/<string:f_type>', 'feed', Api.feed, methods=['GET', 'POST', 'PUT', 'DELETE'])

    # get all friends of a user identified by user_id, defaulting to the id of the active user
    app.add_url_rule('/v1/friends/', 'friends', Api.friends, methods=['GET'])
    app.add_url_rule('/v1/friends/<string:user_id>', 'friends', Api.friends, methods=['GET'])

    # handle message interaction identified by message_id, defaulting to 0 to fetch all messages of a user
    app.add_url_rule('/v1/message/', 'message', Api.messages, methods=['GET', 'PUT'])
    app.add_url_rule('/v1/message/<int:message_id>', 'message', Api.messages, methods=['GET', 'POST', 'PUT', 'DELETE'])

    # handle post interaction identified by post_id
    app.add_url_rule('/v1/post/<int:post_id>', 'post', Api.post, methods=['GET', 'POST', 'PUT', 'DELETE'])

    app.run(host='0.0.0.0', port=9950, debug=True)

"""
Static news feed with friends, etc
Dynamic location-based news feed changes based on your general area with local-friends

Friends have to be accepted/requested
Local-friends are automatically added and then removed when no longer in the general area
"""




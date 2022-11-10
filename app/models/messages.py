from .db import db, environment, SCHEMA, add_prefix_for_prod


class Message(db.Model):

    __tablename__ = 'messages'
    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('users.id')), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    channel_id = db.Column(db.Integer, db.ForeignKey(
        add_prefix_for_prod('channels.id')), nullable=False)
    # created_at = db.Column(db.DateTime, server_default=datetime.now())
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime(
        timezone=True), server_default=db.func.now(), server_onupdate=db.func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "username": self.users.username,
            "user_avatar": self.users.avatar_link,
            "content": self.content,
            "channel_id": self.channel_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    users = db.relationship('User')
    channel = db.relationship('Channel', back_populates='messages')

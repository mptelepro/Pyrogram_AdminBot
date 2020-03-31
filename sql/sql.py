import threading

from sqlalchemy import Column, Integer, UnicodeText, String, ForeignKey, UniqueConstraint, func

from sql.init import BASE, SESSION

class Jinja(BASE):
    __tablename__ = "jinja"
    user_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, primary_key=True)
    jinja = Column(String(32))

    def __init__(self, user_id, chat_id, jinja):
        self.user_id = user_id
        self.chat_id = chat_id
        self.jinja = jinja

Jinja.__table__.create(checkfirst=True)

INSERTION_LOCK = threading.RLock()

def jinja(user_id, chat_id, jinja):
    with INSERTION_LOCK:
        prev_buttons = SESSION.query(Jinja.jinja).filter(Jinja.chat_id == chat_id)
        for btn in prev_buttons:
            SESSION.delete(btn)
        filt = Jinja(user_id, chat_id, jinja)
        SESSION.add(filt)
        SESSION.commit()

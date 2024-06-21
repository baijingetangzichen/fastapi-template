from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from app.config.extend import Base
from app.common.utils import get_uuid


class Role(Base):

    __tablename__ = 'roles'

    id = Column(String, primary_key=True, default=get_uuid())
    name = Column(String(64))
    zh_name = Column(String(32))
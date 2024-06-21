"""用户表aa

Revision ID: 2989081545ee
Revises: 001b354d603a
Create Date: 2024-06-20 11:26:03.507978

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2989081545ee'
down_revision: Union[str, None] = '001b354d603a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###

"""用户表aa

Revision ID: 001b354d603a
Revises: 0a5782cedc03
Create Date: 2024-06-20 11:19:51.827329

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '001b354d603a'
down_revision: Union[str, None] = '0a5782cedc03'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('zh_name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    # ### end Alembic commands ###

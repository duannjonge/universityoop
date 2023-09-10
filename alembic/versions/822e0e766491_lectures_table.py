"""Lectures table

Revision ID: 822e0e766491
Revises: 22d2c9ef2916
Create Date: 2023-09-10 17:46:37.842177

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '822e0e766491'
down_revision: Union[str, None] = '22d2c9ef2916'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table(
    "lecturers",
    sa.Column("id",sa.Integer,primary_key=True,index=True),
    sa.Column("name",sa.String,index=True)





  )

def downgrade() -> None:
  op.drop_table("lecturers")
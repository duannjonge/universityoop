"""Intial Migration

Revision ID: 22d2c9ef2916
Revises: 
Create Date: 2023-09-10 17:35:33.247064

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22d2c9ef2916'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(

    "students",
    sa.Column("id",sa.Integer,primary_key=True,index=True),
    sa.Column("name",sa.String,index=True)

    )


def downgrade() -> None:
    op.drop_table("students")

"""add unit column to student

Revision ID: bef66a915c3d
Revises: d91036e86f84
Create Date: 2023-09-10 17:58:14.523152

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bef66a915c3d'
down_revision: Union[str, None] = 'd91036e86f84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.add_column('students', sa.Column('units', sa.String(length=255), nullable=True))


def downgrade() -> None:
   op.drop_column("students","units")
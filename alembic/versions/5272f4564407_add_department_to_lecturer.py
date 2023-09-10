"""add department to lecturer

Revision ID: 5272f4564407
Revises: bef66a915c3d
Create Date: 2023-09-10 18:28:42.937018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5272f4564407'
down_revision: Union[str, None] = 'bef66a915c3d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
      op.add_column('lecturers', sa.Column('department', sa.String(length=255), nullable=True))
    


def downgrade() -> None:
     op.drop_column("lecturers","department")

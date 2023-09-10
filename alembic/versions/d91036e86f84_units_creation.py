"""Units Creation

Revision ID: d91036e86f84
Revises: 822e0e766491
Create Date: 2023-09-10 17:52:29.403407

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd91036e86f84'
down_revision: Union[str, None] = '822e0e766491'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
      "units",
      sa.Column("id",sa.Integer,primary_key=True,index=True),
      sa.Column("name",sa.String,index=True)
      


   )

def downgrade() -> None:
   op.drop_table("units")

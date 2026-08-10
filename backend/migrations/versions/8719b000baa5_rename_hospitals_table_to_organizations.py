"""rename hospitals table to organizations

Revision ID: 8719b000baa5
Revises: fe5fe9118b6a
Create Date: 2026-08-04 13:32:45.264349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8719b000baa5'
down_revision: Union[str, Sequence[str], None] = 'fe5fe9118b6a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table(
        "hospitals",
        "organizations"
    )


def downgrade() -> None:
    op.rename_table(
        "organizations",
        "hospitals"
    )
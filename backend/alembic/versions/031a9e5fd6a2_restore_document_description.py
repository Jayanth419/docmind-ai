"""restore document description

Revision ID: 031a9e5fd6a2
Revises: b1df5bf93ed9
Create Date: 2026-08-17 19:59:16.277634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '031a9e5fd6a2'
down_revision: Union[str, Sequence[str], None] = 'b1df5bf93ed9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "documents",
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
    )

    op.execute(
        "UPDATE documents "
        "SET description = '' "
        "WHERE description IS NULL"
    )

    op.alter_column(
        "documents",
        "description",
        nullable=False,
    )


def downgrade() -> None:
    op.drop_column(
        "documents",
        "description",
    )

"""repair missing document description

Revision ID: 254263a372f7
Revises: 3a7e4fd82a2a
Create Date: 2026-08-17 20:15:40.591313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '254263a372f7'
down_revision: Union[str, Sequence[str], None] = '3a7e4fd82a2a'
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
        """
        UPDATE documents
        SET description = ''
        WHERE description IS NULL
        """
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
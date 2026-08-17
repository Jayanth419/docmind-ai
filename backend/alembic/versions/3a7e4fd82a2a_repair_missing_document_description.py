"""repair missing document description

Revision ID: 3a7e4fd82a2a
Revises: b8e34b481b11
Create Date: 2026-08-17 20:13:51.764681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a7e4fd82a2a'
down_revision: Union[str, Sequence[str], None] = 'b8e34b481b11'
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
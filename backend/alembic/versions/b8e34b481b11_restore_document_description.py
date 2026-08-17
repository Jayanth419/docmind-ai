"""restore document description

Revision ID: b8e34b481b11
Revises: 031a9e5fd6a2
Create Date: 2026-08-17 20:05:33.741400

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8e34b481b11'
down_revision: Union[str, Sequence[str], None] = '031a9e5fd6a2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

"""create users table

Revision ID: 67f1b0d6021e
Revises: e7f181a11334
Create Date: 2025-09-09 14:52:37.306265

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67f1b0d6021e'
down_revision: Union[str, Sequence[str], None] = 'e7f181a11334'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

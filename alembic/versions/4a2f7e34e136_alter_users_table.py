"""alter users table

Revision ID: 4a2f7e34e136
Revises: 3308b1f661ea
Create Date: 2025-10-29 15:36:25.987248

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a2f7e34e136'
down_revision: Union[str, Sequence[str], None] = '3308b1f661ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE users
        ADD COLUMN gender VARCHAR(50) NOT NULL DEFAULT 'student';
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

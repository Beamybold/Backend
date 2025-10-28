"""alter users table

Revision ID: 3308b1f661ea
Revises: 
Create Date: 2025-10-27 14:14:53.266475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3308b1f661ea'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE users
        ADD COLUMN userType VARCHAR(50) NOT NULL DEFAULT 'student';
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass

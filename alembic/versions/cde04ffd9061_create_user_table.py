"""create_user_table

Revision ID: cde04ffd9061
Revises: 
Create Date: 2021-08-21 17:50:21.540396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cde04ffd9061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('user_name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('users')

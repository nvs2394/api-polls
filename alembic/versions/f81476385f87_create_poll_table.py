"""create_poll_table

Revision ID: f81476385f87
Revises: cde04ffd9061
Create Date: 2021-08-21 17:51:25.048358

"""
from alembic import op
import sqlalchemy as sa
import enum

# revision identifiers, used by Alembic.
revision = 'f81476385f87'
down_revision = 'cde04ffd9061'
branch_labels = None
depends_on = None


class PollTypeEnum(enum.Enum):
    text = 'TEXT'
    image = 'IMAGE'


def upgrade():
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(PollTypeEnum), nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('is_add_choices_active',
                  sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('polls')

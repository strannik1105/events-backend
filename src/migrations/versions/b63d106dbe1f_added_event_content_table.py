"""Added event content table

Revision ID: b63d106dbe1f
Revises: c5793bec67c2
Create Date: 2024-09-27 20:15:21.300606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b63d106dbe1f'
down_revision = 'c5793bec67c2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE SCHEMA event_content")
    op.create_table('event_content',
    sa.Column('sid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('event_content_type_sid', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['event_content_type_sid'], ['event_content_type.event_content_type.sid'], ),
    sa.PrimaryKeyConstraint('sid'),
    schema='event_content'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('event_content', schema='event_content')
    # ### end Alembic commands ###

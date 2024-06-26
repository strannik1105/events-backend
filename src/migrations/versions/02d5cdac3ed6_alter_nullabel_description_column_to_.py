"""alter_nullabel_description_column_to_event_content_table

Revision ID: 02d5cdac3ed6
Revises: 74a4163caa1c
Create Date: 2024-06-17 21:28:50.760719

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "02d5cdac3ed6"
down_revision = "74a4163caa1c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "event_content",
        "name",
        existing_type=sa.VARCHAR(),
        comment="Event content name",
        existing_comment="Event name",
        existing_nullable=False,
    )
    op.alter_column(
        "event_content",
        "description",
        existing_type=sa.VARCHAR(),
        nullable=True,
        comment="Event content description",
        existing_comment="Event description",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "event_content",
        "description",
        existing_type=sa.VARCHAR(),
        nullable=False,
        comment="Event description",
        existing_comment="Event content description",
    )
    op.alter_column(
        "event_content",
        "name",
        existing_type=sa.VARCHAR(),
        comment="Event name",
        existing_comment="Event content name",
        existing_nullable=False,
    )
    # ### end Alembic commands ###

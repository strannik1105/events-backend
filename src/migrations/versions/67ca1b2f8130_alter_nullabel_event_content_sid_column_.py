"""alter_nullabel_event_content_sid_column_to_event_pull_table

Revision ID: 67ca1b2f8130
Revises: 77d3997d3937
Create Date: 2024-06-17 12:31:15.004866

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "67ca1b2f8130"
down_revision = "77d3997d3937"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "event_pull",
        "event_content_sid",
        existing_type=sa.UUID(),
        nullable=True,
        existing_comment="Event content SID",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "event_pull",
        "event_content_sid",
        existing_type=sa.UUID(),
        nullable=False,
        existing_comment="Event content SID",
    )
    # ### end Alembic commands ###

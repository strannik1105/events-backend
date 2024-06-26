"""create_event_address_table

Revision ID: fc8ecdce47d8
Revises: a8c8020a45ca
Create Date: 2024-06-13 00:24:49.034177

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "fc8ecdce47d8"
down_revision = "a8c8020a45ca"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "event_address",
        sa.Column("sid", sa.Uuid(), nullable=False),
        sa.Column(
            "address", sa.String(), nullable=False, comment="Event address"
        ),
        sa.Column("event_sid", sa.Uuid(), nullable=False, comment="Event SID"),
        sa.Column(
            "event_content_sid",
            sa.Uuid(),
            nullable=False,
            comment="Event content SID",
        ),
        sa.Column(
            "start_at", sa.DateTime(), nullable=False, comment="Event start at"
        ),
        sa.Column(
            "end_at", sa.DateTime(), nullable=False, comment="Event finish at"
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False,
            comment="Record creating time",
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False,
            comment="Record updating time",
        ),
        sa.ForeignKeyConstraint(
            ["event_content_sid"],
            ["events.event_content.sid"],
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["event_sid"], ["events.event.sid"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="events",
        comment="Table with all event addresses",
    )
    op.create_index(
        op.f("ix_events_event_address_event_content_sid"),
        "event_address",
        ["event_content_sid"],
        unique=False,
        schema="events",
    )
    op.create_index(
        op.f("ix_events_event_address_event_sid"),
        "event_address",
        ["event_sid"],
        unique=False,
        schema="events",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_events_event_address_event_sid"),
        table_name="event_address",
        schema="events",
    )
    op.drop_index(
        op.f("ix_events_event_address_event_content_sid"),
        table_name="event_address",
        schema="events",
    )
    op.drop_table("event_address", schema="events")
    # ### end Alembic commands ###

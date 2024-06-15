"""create_subscribe_table

Revision ID: f79a36eb539a
Revises: 51987fae3b6d
Create Date: 2024-06-13 00:27:02.505968

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "f79a36eb539a"
down_revision = "51987fae3b6d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "subscribe",
        sa.Column("sid", sa.Uuid(), nullable=False),
        sa.Column("user_sid", sa.Uuid(), nullable=False, comment="User SID"),
        sa.Column(
            "subscriber_sid",
            sa.Uuid(),
            nullable=False,
            comment="Subscriber SID",
        ),
        sa.Column(
            "is_notify",
            sa.Boolean(),
            server_default="true",
            nullable=False,
            comment="Notify status",
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
            ["subscriber_sid"], ["users.user.sid"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["user_sid"], ["users.user.sid"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("sid"),
        schema="metrics",
        comment="Table with all subscribers",
    )
    op.create_index(
        op.f("ix_metrics_subscribe_subscriber_sid"),
        "subscribe",
        ["subscriber_sid"],
        unique=False,
        schema="metrics",
    )
    op.create_index(
        op.f("ix_metrics_subscribe_user_sid"),
        "subscribe",
        ["user_sid"],
        unique=False,
        schema="metrics",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_metrics_subscribe_user_sid"),
        table_name="subscribe",
        schema="metrics",
    )
    op.drop_index(
        op.f("ix_metrics_subscribe_subscriber_sid"),
        table_name="subscribe",
        schema="metrics",
    )
    op.drop_table("subscribe", schema="metrics")
    # ### end Alembic commands ###
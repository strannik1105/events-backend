"""create_is_event_column_to_role_table

Revision ID: 6815a7a6f8b3
Revises: 7e7764d8b9db
Create Date: 2024-06-16 22:04:48.875067

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "6815a7a6f8b3"
down_revision = "7e7764d8b9db"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "role",
        sa.Column(
            "is_event",
            sa.Boolean(),
            nullable=False,
            comment="Role event status",
        ),
        schema="security",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("role", "is_event", schema="security")
    # ### end Alembic commands ###

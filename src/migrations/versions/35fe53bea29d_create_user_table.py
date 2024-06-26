"""create_user_table

Revision ID: 35fe53bea29d
Revises: 26a867c42173
Create Date: 2024-06-12 22:09:58.185384

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "35fe53bea29d"
down_revision = "26a867c42173"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("sid", sa.Uuid(), nullable=False),
        sa.Column(
            "first_name",
            sa.String(),
            nullable=False,
            comment="User first name",
        ),
        sa.Column(
            "middle_name",
            sa.String(),
            nullable=True,
            comment="User middle name",
        ),
        sa.Column(
            "last_name", sa.String(), nullable=False, comment="User last name"
        ),
        sa.Column("email", sa.String(), nullable=False, comment="User email"),
        sa.Column(
            "hashed_password",
            sa.String(),
            nullable=False,
            comment="User hashed password",
        ),
        sa.Column(
            "telegram_id",
            sa.BIGINT(),
            nullable=True,
            comment="User telegram id",
        ),
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default="true",
            nullable=False,
            comment="User active status",
        ),
        sa.Column(
            "is_verified",
            sa.Boolean(),
            server_default="false",
            nullable=False,
            comment="User verified status",
        ),
        sa.Column(
            "last_login_at",
            sa.DateTime(),
            nullable=True,
            comment="User last login at",
        ),
        sa.Column(
            "role_label", sa.SMALLINT(), nullable=False, comment="Role label"
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
            ["role_label"], ["security.role.label"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("sid"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("telegram_id"),
        schema="users",
        comment="Table with all users",
    )
    op.create_index(
        op.f("ix_users_user_role_label"),
        "user",
        ["role_label"],
        unique=False,
        schema="users",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_users_user_role_label"), table_name="user", schema="users"
    )
    op.drop_table("user", schema="users")
    # ### end Alembic commands ###

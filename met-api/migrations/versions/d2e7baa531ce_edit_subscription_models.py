"""edit_subscription_models

Revision ID: d2e7baa531ce
Revises: d152f85734f9
Create Date: 2023-06-01 21:09:11.767623

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd2e7baa531ce'
down_revision = 'd152f85734f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('engagement_id', sa.Integer(), nullable=True))
    op.drop_constraint('subscription_email_verification_id_fkey', 'subscription', type_='foreignkey')
    op.drop_column('subscription', 'email_verification_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscription', sa.Column('email_verification_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('subscription_email_verification_id_fkey', 'subscription', 'email_verification', ['email_verification_id'], ['id'])
    op.drop_column('subscription', 'engagement_id')
    # ### end Alembic commands ###

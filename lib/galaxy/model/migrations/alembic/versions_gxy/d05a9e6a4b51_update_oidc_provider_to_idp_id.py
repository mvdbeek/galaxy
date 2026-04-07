"""Update oidc_user_authnz_tokens.provider to use config key names (idp_id)

Previously, the `provider` column stored PSA backend names such as
`google-openidconnect`, `life_science`, `e-infra_cz` etc.  After this
migration the column stores the lowercased provider name as specified in
`oidc_backends_config.xml` (e.g. `google`, `lifescience`, `einfracz`),
which matches the default `idp_id` for each provider.

Revision ID: d05a9e6a4b51
Revises: 566b691307a5
Create Date: 2025-04-07 00:00:00.000000

"""

from alembic import op
from sqlalchemy.sql import text

# revision identifiers, used by Alembic.
revision = "d05a9e6a4b51"
down_revision = "566b691307a5"
branch_labels = None
depends_on = None

# Map from old PSA backend name -> new provider key (idp_id default = name.lower())
# Only providers where the PSA backend name differs from the config key need updating.
PROVIDER_NAME_MAP = {
    "google-openidconnect": "google",
    "life_science": "lifescience",
    "e-infra_cz": "einfracz",
    "infraproxy": "nfdi",
    "okta-openidconnect": "okta",
    "azuread-v2-tenant-oauth2": "azure",
    "egi-checkin": "egi_checkin",
}


def upgrade():
    conn = op.get_bind()
    for old_name, new_name in PROVIDER_NAME_MAP.items():
        conn.execute(
            text("UPDATE oidc_user_authnz_tokens SET provider = :new WHERE provider = :old"),
            {"old": old_name, "new": new_name},
        )


def downgrade():
    conn = op.get_bind()
    for old_name, new_name in PROVIDER_NAME_MAP.items():
        conn.execute(
            text("UPDATE oidc_user_authnz_tokens SET provider = :old WHERE provider = :new"),
            {"old": old_name, "new": new_name},
        )

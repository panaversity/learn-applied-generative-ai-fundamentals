from starlette.config import Config
from starlette.datastructures import Secret
from uuid import UUID

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

# Custom GPTs
ENVIRONMENT: str = "development"
API_V1_STR: str = "/api/v1"
DEFAULT_QUARTER_FEE: int = 7000

EMAILS_FROM_NAME: str = "Panaversity"
EMAILS_FROM_EMAIL: str = "hello@panaversity.com"

EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 1

SECRET_KEY: str = "changethis"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

PROGRAM_ID: UUID = UUID("eed86350-cb30-469d-9e4d-f7f42caaab46")

SMTP_HOST="smtp.gmail.com"
SMTP_TLS=True
SMTP_SSL=False
SMTP_PORT=587

SMTP_USER=config("SMTP_USER", cast=str, default=None)
SMTP_PASSWORD=config("SMTP_PASSWORD", cast=str, default=None)

SERVER_URL = config("ONBOARDING_SERVER_URL", default="http://localhost:9010")

DATABASE_URL = config("DATABASE_URL", cast=Secret)

# Payments
STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", cast=Secret, default=None)
STRIPE_WEBHOOK_SECRET = config("STRIPE_WEBHOOK_SECRET", cast=Secret, default=None)

PANAVERSITY_PORTAL_GPT = config("PANAVERSITY_PORTAL_GPT", cast=str, default=None)
PANAVERSITY_ONBOARDING_GPT = config("PANAVERSITY_ONBOARDING_GPT", cast=str, default=None)

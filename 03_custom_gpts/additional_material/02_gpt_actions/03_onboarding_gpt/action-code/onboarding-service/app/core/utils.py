import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import emails  # type: ignore
from jinja2 import Template

from app import settings
import random

def generate_verification_code() -> str:
    """Generates a 6-digit verification code."""
    return str(random.randint(100000, 999999))


@dataclass
class EmailData:
    html_content: str
    subject: str


def render_email_template(*, template_name: str, context: dict[str, Any]) -> str:
    template_str = (
        Path(__file__).parent.parent / "email-templates" / "build" / template_name
    ).read_text()
    html_content = Template(template_str).render(context)
    return html_content


def send_email(
    *,
    email_to: str,
    subject: str = "",
    html_content: str = "",
) -> None:
    message = emails.Message(
        subject=subject,
        html=html_content,
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL),
    )
    smtp_options = {"host": settings.SMTP_HOST, "port": settings.SMTP_PORT}
    if settings.SMTP_TLS:
        smtp_options["tls"] = True
    elif settings.SMTP_SSL:
        smtp_options["ssl"] = True
    if settings.SMTP_USER:
        smtp_options["user"] = settings.SMTP_USER
    if settings.SMTP_PASSWORD:
        smtp_options["password"] = settings.SMTP_PASSWORD
    # print("smtp_options", smtp_options)
    response = message.send(to=email_to, smtp=smtp_options)
    logging.info(f"send email result: {response}")


def generate_new_account_email(
    email_to: str
) -> EmailData:
    project_name = settings.EMAILS_FROM_NAME
    subject = f"Welcome to {project_name}"
    html_content = render_email_template(
        template_name="new_account.html",
        context={
            "project_name": settings.EMAILS_FROM_NAME,
            "message": f"Congratulations on Registering your new Account using email: {email_to}",
            "email": email_to,
            "onboarding_link": settings.PANAVERSITY_ONBOARDING_GPT,
            "visit_portal": settings.PANAVERSITY_PORTAL_GPT,
        },
    )
    return EmailData(html_content=html_content, subject=subject)


def send_verification_code_email(email_to: str, code: str) -> None:
    """
    Sends a verification code email to the user.

    Args:
        email_to (str): The recipient's email address.
        code (str): The verification code to send.
    """
    project_name = settings.EMAILS_FROM_NAME
    subject = f"{project_name} - Your Verification Code"
    html_content = render_email_template(
        template_name="verification_code.html",
        context={
            "project_name": settings.EMAILS_FROM_NAME,
            "email": email_to,
            "verification_code": code,
        },
    )
    send_email(email_to=email_to, subject=subject, html_content=html_content)
    logging.info(f"Verification code email sent to {email_to}")
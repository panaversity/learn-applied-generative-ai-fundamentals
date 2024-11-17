import stripe
from app import settings
from typing import Any
from app import settings

def generate_checkout_session(quarter_enrollment: Any, student_email: str, quarter: int, enrollment: Any | None = None):
    # Generate checkout session URL
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'pkr',
                    'product_data': {
                        'name': 'Quarter 1 Voucher',
                        'description': 'Voucher for Quarter 1',
                    },
                    # Stripe expects amount in cents,
                    'unit_amount': settings.DEFAULT_QUARTER_FEE * 100,
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=settings.PANAVERSITY_PORTAL_GPT,
        cancel_url=f'{settings.PANAVERSITY_ONBOARDING_GPT}',
        metadata={
            'quarter_enrollment_id': quarter_enrollment.id,
            'student_email': student_email,
            'program_id': enrollment.program_id if enrollment else settings.PROGRAM_ID,
            'quarter': quarter
        }
    )

    return checkout_session

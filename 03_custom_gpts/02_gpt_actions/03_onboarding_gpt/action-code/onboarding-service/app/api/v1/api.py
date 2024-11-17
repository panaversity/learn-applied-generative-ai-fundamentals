from fastapi import APIRouter
from app.api.v1.routes import student, enrollment, code_verification

api_router = APIRouter()

api_router.include_router(
    code_verification.router, prefix="/verification", tags=["Code Verification"])
api_router.include_router(
    student.router, prefix="/students", tags=["Registration"])
api_router.include_router(
    enrollment.router, prefix="/enrollments", tags=["Enrollments"])

from sqlmodel import Session
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Annotated
from jose import JWTError, jwt
from pydantic import ValidationError

from app.core.db_eng import engine
from app import settings
from app.models.base import TokenPayload, DecodedTokenPayload
from app.core import security


# Define the security scheme
http_bearer = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    token = credentials.credentials
    print(f"Token: {token}")
    # Implement your token verification logic here
    # For example, decode a JWT token or lookup in a database
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        print(f"Payload: {payload}")
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
            detail={"error": "invalid_token",
                    "error_description": "The access token expired"}
        )

    if token_data.sub is None:
        print("Token sub is None")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
            detail={"error": "invalid_token",
                    "error_description": "The access token expired"}
        )

    return DecodedTokenPayload(email=token_data.sub)


TokenDep = Annotated[DecodedTokenPayload, Depends(verify_token)]


def get_session():
    with Session(engine) as session:
        yield session


DBSessionDep = Annotated[Session, Depends(get_session)]


def body_access_token(token: str):
    print(f"Token: {token}")
    # Implement your token verification logic here
    # For example, decode a JWT token or lookup in a database
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        print(f"Payload: {payload}")
        token_data = TokenPayload(**payload)
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
            detail={"error": "invalid_token",
                    "error_description": "The access token expired"}
        )

    if token_data.sub is None:
        print("Token sub is None")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            headers={"WWW-Authenticate": "Bearer"},
            detail={"error": "invalid_token",
                    "error_description": "The access token expired"}
        )

    return DecodedTokenPayload(email=token_data.sub)

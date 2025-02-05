class Config:
    PROJECT_NAME: str = "API com Copilot"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "A FastAPI application for task management."
    DEBUG: bool = True
    DATABASE_URL: str = "sqlite:///./memory.db"  # Placeholder for local storage configuration
    ALLOWED_HOSTS: list = ["*"]  # Adjust as necessary for production settings

config = Config()
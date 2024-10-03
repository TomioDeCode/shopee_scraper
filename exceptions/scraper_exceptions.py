# exceptions/scraper_exceptions.py


class ScraperException(Exception):
    """Base exception for scraper-related errors."""

    pass


class LoginError(ScraperException):
    """Raised when there's an error during the login process."""

    pass


class ProductExtractionError(ScraperException):
    """Raised when there's an error extracting product data."""

    pass


class NetworkError(ScraperException):
    """Raised when there's a network-related error."""

    pass

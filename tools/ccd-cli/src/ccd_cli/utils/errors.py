"""
CCD Error Classes

Custom exception classes for CCD CLI.
"""


class CCDError(Exception):
    """
    Base exception class for CCD CLI errors.
    
    This exception is raised when CCD-specific errors occur,
    such as validation failures, configuration issues, or
    other CCD-related problems.
    """
    
    def __init__(self, message: str, details: str = None, code: str = None):
        """
        Initialize CCD error.
        
        Args:
            message: Error message
            details: Additional error details
            code: Error code for programmatic handling
        """
        self.message = message
        self.details = details
        self.code = code
        
        # Build full message
        full_message = message
        if details:
            full_message += f": {details}"
        if code:
            full_message += f" (Code: {code})"
        
        super().__init__(full_message)


class ValidationError(CCDError):
    """Raised when CCD validation fails."""
    
    def __init__(self, message: str, field: str = None, value: str = None):
        """
        Initialize validation error.
        
        Args:
            message: Validation error message
            field: Field that failed validation
            value: Value that caused validation failure
        """
        details = None
        if field and value:
            details = f"Field '{field}' with value '{value}'"
        elif field:
            details = f"Field '{field}'"
        
        super().__init__(message, details, "VALIDATION_ERROR")


class ConfigurationError(CCDError):
    """Raised when CCD configuration is invalid."""
    
    def __init__(self, message: str, config_path: str = None):
        """
        Initialize configuration error.
        
        Args:
            message: Configuration error message
            config_path: Path to the configuration file
        """
        details = None
        if config_path:
            details = f"Configuration file: {config_path}"
        
        super().__init__(message, details, "CONFIGURATION_ERROR")


class GenerationError(CCDError):
    """Raised when CCD generation fails."""
    
    def __init__(self, message: str, file_path: str = None, operation: str = None):
        """
        Initialize generation error.
        
        Args:
            message: Generation error message
            file_path: File that caused generation failure
            operation: Operation that failed
        """
        details = None
        if file_path and operation:
            details = f"Operation '{operation}' on file '{file_path}'"
        elif file_path:
            details = f"File: {file_path}"
        elif operation:
            details = f"Operation: {operation}"
        
        super().__init__(message, details, "GENERATION_ERROR")


class SchemaError(CCDError):
    """Raised when JSON schema validation fails."""
    
    def __init__(self, message: str, schema_path: str = None, validation_errors: list = None):
        """
        Initialize schema error.
        
        Args:
            message: Schema error message
            schema_path: Path to the schema file
            validation_errors: List of validation errors
        """
        details = None
        if schema_path and validation_errors:
            details = f"Schema: {schema_path}, Errors: {len(validation_errors)}"
        elif schema_path:
            details = f"Schema: {schema_path}"
        elif validation_errors:
            details = f"Validation errors: {len(validation_errors)}"
        
        super().__init__(message, details, "SCHEMA_ERROR")


class FileError(CCDError):
    """Raised when file operations fail."""
    
    def __init__(self, message: str, file_path: str = None, operation: str = None):
        """
        Initialize file error.
        
        Args:
            message: File error message
            file_path: Path to the file
            operation: Operation that failed
        """
        details = None
        if file_path and operation:
            details = f"Operation '{operation}' on file '{file_path}'"
        elif file_path:
            details = f"File: {file_path}"
        elif operation:
            details = f"Operation: {operation}"
        
        super().__init__(message, details, "FILE_ERROR")


class GitError(CCDError):
    """Raised when Git operations fail."""
    
    def __init__(self, message: str, repository_path: str = None, git_command: str = None):
        """
        Initialize Git error.
        
        Args:
            message: Git error message
            repository_path: Path to the repository
            git_command: Git command that failed
        """
        details = None
        if repository_path and git_command:
            details = f"Command '{git_command}' in repository '{repository_path}'"
        elif repository_path:
            details = f"Repository: {repository_path}"
        elif git_command:
            details = f"Git command: {git_command}"
        
        super().__init__(message, details, "GIT_ERROR")

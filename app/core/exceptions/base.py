class AppException(Exception):
    
    def __init__(self,message:str,status_code: int = 400,error_type: str = "App Error",error_details:list = None):
        self.message = message
        self.status_code = status_code
        self.error_type = error_type
        self.error_details = error_details or []
from fastapi import HTTPException, status


class DuplicateTimestampError(HTTPException):
    def __init__(self, message:str):
        self.message = message
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=self.message)

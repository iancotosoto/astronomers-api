from flask import jsonify

# Functions
def generate_response(status: str, message: str, data: list, code: int):
    """
    Generate response for endpoints services
    """
    return jsonify( {
                        "status": status,
                        "message": message,
                        "data": data,
                        "code": code
                    }), code
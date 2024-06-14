from flask import jsonify

def generate_response(status: str, message: str, data: list, code: int):
        return jsonify( {
                            "status": status,
                            "message": message,
                            "data": data,
                            "code": code
                        }), code
from apistar import http, types


def AcceptOrigin(method: http.Method, response: types.ReturnValue):
    response.headers.append("Access-Control-Allow-Origin", "*")
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS,HEADERS"
    response.headers["Access-Control-Allow-Headers"] = "Authorization"
    response.headers["Access-Control-Expose-Headers"] = "*"
    if method.lower() == "options":
        response.status = 200
    return response

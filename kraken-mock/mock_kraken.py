from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route that returns mock data and prints request information
@app.route('/', methods=['GET', 'POST'])
def get_mock_data():
    # Access request headers
    request_headers = dict(request.headers)

    # Access request body (for POST requests)
    request_body = request.get_json()

    # Print request headers and body
    print("Request Headers:", request_headers)
    print("Request Body:", request_body)

    mock_data = {'message': 'This is mock data'}
    return jsonify({"request_header": request_headers, "request_body": request_body})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9001)  # Run the Flask app on port 8000
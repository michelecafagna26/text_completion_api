from text_completion_service.__main__ import app, main
from flask_cors import CORS


if __name__ == "__main__":
    CORS(app.app)
    app.run(port=9994)
else:
    main()
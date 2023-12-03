# is it healthy? | API

<div align="center">
  <img src="https://raw.githubusercontent.com/hirusha-adi/is-it-healthy/main/artwork/android/res/mipmap-xxxhdpi/ic_launcher.png" width="250">
  <h2>is it healthy?</h2>
</div>

This is a FastAPI application providing an API to retrieve and create data about various items. The data is sourced from a JSON file and can be accessed easily!

## Getting Started

### Prerequisites

- Python (3.7 or higher)
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/is-it-healthy/api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi-data-api
   ```

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

Start the FastAPI application using `uvicorn`:

```bash
uvicorn api:app --reload
```

( where api is the filename (`api.py`) )

The server will be running at http://127.0.0.1:8000.

Visit the Swagger UI for interactive documentation: http://127.0.0.1:8000/docs

### API Endpoints

- **GET /get_data/{item_id}**: Retrieve information about a specific item.

  - Curl:

    ```bash
    curl -X 'GET' \
    'http://127.0.0.1:8000/get_data/102?include_code=true&include_name=true&include_href=true&include_function=true&include_more_info=true' \
    -H 'accept: application/json'
    ```

  - Request URL

    ```
    http://127.0.0.1:8000/get_data/102?include_code=true&include_name=true&include_href=true&include_function=true&include_more_info=true
    ```

  - Server response

    ```json
    {
      "code": "E102",
      "name": "Tartrazine",
      "href": "e102.htm",
      "function": "Yellow colour, azo dye",
      "more_info": {
        "origin": "Synthetic azo dye. See  for a background on azo dyes.",
        "characteristics": "Yellow food colour. Very soluble in water.",
        "products": "Many different products.",
        "daily_intake": "Up to 7.5 mg/kg body weight.",
        "side_effects": "Tartrazine is an azo dye. No side effects are known for pure tartrazine, except in people who are intolerant to salicylates (aspirin, berries, fruits); in that case tartrazine also induces intolerance symptoms. In combination with benzoates (E210-215), tartrazine is implicated in a large percentage of cases of ADHD syndrome (hyperactivity) in children. Asthmatics may also experience symptoms following consumption of tartrazine, as it is a known histamine-liberating agent.",
        "dietary_restrictions": "None; E102 can be consumed by all religious groups, vegans and vegetarians."
      }
    }
    ```

- **GET /list_items**: Retrieve information about all items.

### Development Environment

For development, it is recommended to use the `--reload` option with `uvicorn` to enable automatic code reloading:

```bash
uvicorn main:app --reload
```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [Requests](https://docs.python-requests.org/en/latest/)

# Generate Synthetic Data with AI and Blockchain

This project is designed to generate synthetic data using AI and blockchain technologies. It leverages OpenAI's GPT-3.5-turbo model to generate realistic data based on provided examples and uses FastAPI to serve the data through a web API.

## Technologies Used

- OpenAI
- Python
- FastAPI
- PostgreSQL
- Docker
- GitHub Actions

## Project Structure
![Project Structure](<project_structure.png>)

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/zczqas/Synthetic-Data-Generator.git
    cd Synthetic-Data-Generator
    ```

2. Create and configure the `.env` file:
    ```sh
    cp .env.example .env
    ```

3. Build and run the Docker containers:
    ```sh
    docker-compose up --build
    ```

## API Endpoints

### CSV Generation

- **GET /api/v1/csv/prompt**
    - Query Parameters:
        - [category](string): The category for CSV generation.
    - Response: Returns a CSV file based on the specified category.

### Data Generation

- **POST /api/v1/data/generate**
    - Form Data:
        - [file](UploadFile): Example data in CSV format.
        - [data_type](string): Type of data to generate (regular/timeseries).
        - [num_rows](int): Number of rows to generate.
        - [batch_size](int): Batch size for LLM calls (default: 200).
    - Response: Returns a CSV file with generated synthetic data.

## Configuration

Configuration settings are managed in the `.env` file. Key settings include:

- `DATABASE_HOST`
- `DATABASE_PORT`
- `DATABASE_NAME`
- `DATABASE_USER`
- `DATABASE_PASSWORD`
- `SQLALCHEMY_DATABASE_URL`
- `ASYNC_SQLALCHEMY_DATABASE_URL`
- `SECRET_KEY`
- `ALGORITHM`
- `ACCESS_TOKEN_EXPIRE_MINUTES`
- `REFRESH_TOKEN_TIME_IN_MINUTES`
- `ANTHROPIC_API_KEY`
- `GENERATED_MEDIA_PATH`
- `GENERATED_CSV_PATH`

## Running Tests

You can use the [test_main.http]file to test the API endpoints using an HTTP client like [HTTPie](https://httpie.io/) or [Postman](https://www.postman.com/).
You can also use in-built swagger UI to test the API endpoints.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

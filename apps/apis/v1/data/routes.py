import csv
from io import StringIO
from fastapi import (
    APIRouter,
    HTTPException,
    File,
    Response,
    UploadFile,
    status,
    Form,
)
import anthropic

from apps.apis.v1.data.prompt import generation_prompt, timeseries_prompt
from apps.config.settings import API_KEY
from apps.apis.v1.data.helpers import (
    infer_data_type,
    parse_and_validate_row,
    ensure_uniqueness,
    sort_timeseries_data,
)

router = APIRouter(prefix="/data", tags=["Data"])

API_ENDPOINT = "https://api.claude.ai/v3/generate"

@router.post("/generate")
async def generate_data(
    file: UploadFile = File(...), # Please provide the example data in CSV format
    data_type: str = Form(...), # Enter the type of data to generate (regular/timeseries):
    num_rows: int = Form(...), # Enter the desired number of rows to generate
    batch_size: int = Form(200), # Enter the batch size for LLM calls (default: 200):
):
    example_data = await file.read()
    example_data = example_data.decode("utf-8")

    try:
        client = anthropic.Client(api_key=API_KEY)
        structured_data = []

        for i in range(0, num_rows, batch_size):
            remaining_rows = num_rows - i
            batch_num_rows = min(remaining_rows, batch_size)

            if data_type == "timeseries":
                prompt = timeseries_prompt
            else:
                prompt = generation_prompt

            batch_prompt = prompt.format(num_rows=batch_num_rows)

            try:
                response = client.messages.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f"{anthropic.HUMAN_PROMPT} Example data:\n{example_data}\n\n{batch_prompt} {anthropic.AI_PROMPT}",
                        }
                    ],
                    model="claude-3-opus-20240229",  # Ensure this model identifier is correct
                    # max_tokens_to_sample=1024,
                    max_tokens=1024,
                )
                generated_data = response.content[0].text

                if not generated_data:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Failed to generate data",
                    )
            except Exception as e:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f"An error occurred while calling the API: {e}"
                ) from e

            csv_start_index = generated_data.find("\n")
            if csv_start_index != -1:
                generated_data = generated_data[csv_start_index + 1:]

            rows = generated_data.strip().split("\n")
            headers = rows[0].split(",")
            for row in rows[1:]:
                values = row.split(",")
                structured_data.append(dict(zip(headers, values)))

        data = []
        unique_values = {}
        data_types = {}

        for row in structured_data:
            for field, value in row.items():
                if field not in data_types:
                    data_types[field] = infer_data_type(value)

            row = parse_and_validate_row(row, data_types)
            row = ensure_uniqueness(row, unique_values, data_type, headers)
            data.append(row)

        unique_data = [dict(t) for t in {tuple(d.items()) for d in data}]

        if data_type == "timeseries":
            unique_data = sort_timeseries_data(unique_data, headers)

        csv_output = StringIO()

        writer = csv.DictWriter(csv_output, fieldnames=headers)
        writer.writeheader()
        writer.writerows(unique_data)

        csv_content = csv_output.getvalue()

        response = Response(
            content=csv_content,
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=synthetic_data.csv"
            }
        )
        return response

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while generating synthetic data: {e}"
        ) from e

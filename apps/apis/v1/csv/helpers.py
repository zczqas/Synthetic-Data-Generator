import uuid
import csv

from fastapi import HTTPException, status

from mech_client.interact import interact, ConfirmationType

from apps.apis.v1.csv.prompt import CSV_PROMPT_TEXT
from apps.config.settings import GENERATED_CSV_PATH


def generate_csv(category):
    try:
        result = interact(
            prompt=CSV_PROMPT_TEXT.format(category=category),
            agent_id=6,
            tool="openai-gpt-3.5-turbo",
            chain_config="gnosis",
            confirmation_type=ConfirmationType.ON_CHAIN,
            # looks for file cannot directly pass the key
            private_key_path="ethereum_private_key.txt",
        )

        csv_data = result["result"]

        filename_id = uuid.uuid4()
        filename = f"{GENERATED_CSV_PATH}/{category.lower().replace(' ', '_')}_{filename_id}_data.csv"
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for row in csv_data.split("\n"):
                writer.writerow(row.split(", "))

        return filename

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while generating the CSV file: {e}",
        ) from e

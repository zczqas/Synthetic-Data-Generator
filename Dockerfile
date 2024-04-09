FROM python:3.10.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh && chown root:root entrypoint.sh


# RUN chmod +x ./entrypoint.sh
EXPOSE 8000


ENTRYPOINT ["/bin/bash", "./entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

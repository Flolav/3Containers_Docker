FROM python:3.10-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

COPY . .

CMD streamlit run app.py

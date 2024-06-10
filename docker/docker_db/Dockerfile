FROM python:3.12
RUN pip install poetry 
WORKDIR /code 
ADD ./pyproject.toml /code/
ADD ./docker_db /code/docker_db 
# COPY pyproject.toml ./
# COPY . . 
RUN poetry install 
CMD ["poetry", "run", "uvicorn", "docker_db.main:app", "--reload", "--host", "0.0.0. 0" ]
#ENTRYPOINT command is often used in order to avoid over writing of the CMD file while working inside the contianers


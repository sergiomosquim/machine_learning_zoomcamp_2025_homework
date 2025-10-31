FROM agrigorev/zoomcamp-model:2025

# Copy the 'uv' and 'uvx' executables from the latest uv image into /bin/ in this image
# 'uv' is a fast Python package installer and environment manager
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory inside the container to /code
WORKDIR /code

# directory for uv virtual environment 
ENV PATH="/code/.venv/bin:$PATH"

# copy project data
COPY "pyproject.toml" "uv.lock" ".python-version" "predict_docker.py" ./

# Install dependencies
RUN uv sync --locked

# expose port 9696 set in the FastAPI
EXPOSE 9696

# Set up entrypoint
COPY "runapp.sh" ./
RUN chmod +x runapp.sh

ENTRYPOINT ["/code/runapp.sh"]
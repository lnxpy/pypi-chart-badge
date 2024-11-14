# Set the base image to the minimal Python 3.12 slim image
FROM python:3.12-slim

# Copy only the necessary binaries from uv
COPY --from=ghcr.io/astral-sh/uv:0.5.1 /uv /uvx /bin/

# Set environment variable early to take advantage of layer caching
ENV UV_PROJECT_ENVIRONMENT="/usr/local/"

# Set the working directory to /action
WORKDIR /action

# importing the action
COPY . .

# running the script.sh
RUN if [ -f script.sh ]; then sh script.sh; fi

# Install project dependencies first for better caching
RUN uv sync --frozen --no-cache

# Specify the command to run main.py with uv
CMD [ "uv", "run", "main.py" ]

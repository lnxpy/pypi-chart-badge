# Setting the base-image
FROM python:3.12-slim

# Copy only the necessary binaries from uv
COPY --from=ghcr.io/astral-sh/uv:0.5.1 /uv /uvx /bin/

# Set the working directory to /action
WORKDIR /action

# Import the action
COPY . .

# Run the pre-script.sh
RUN [ -f pre-script.sh ] && sh pre-script.sh || true

# Install action dependencies
RUN uv pip install . --system

# running the post-script.sh
RUN [ -f post-script.sh ] && sh post-script.sh || true

# Specify the command to run main.py with uv
CMD [ "python", "/action/main.py" ]

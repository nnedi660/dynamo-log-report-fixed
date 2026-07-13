# Pre-approved base image — pinned by digest (required rule)
FROM public.ecr.aws/docker/library/python:3.13-slim-bookworm@sha256:01f42367a0a94ad4bc17111776fd66e3500c1d87c15bbd6055b7371d39c124fb

WORKDIR /app

# Install ONLY runtime/test dependencies — NO apt version pinning
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Pin Python/test dependencies exactly
RUN pip install --no-cache-dir \
    pytest==8.4.1

# Copy ONLY input data — NEVER copy instruction.md, solution/, tests/
COPY data/ /app/data/

# Pre-create output directory
RUN mkdir -p /app

CMD ["/bin/bash"]

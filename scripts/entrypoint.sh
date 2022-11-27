#!/bin/bash

exec uvicorn main:app --app-dir shortly/app/entrypoints/http/fastapi \
                      --host 0.0.0.0 \
                      --port 8000 \
                      --header server:HIDDEN;

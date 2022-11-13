#!/bin/bash

exec uvicorn main:app --app-dir shortly/app \
                      --host 0.0.0.0 \
                      --port 8000 \
                      --header server:HIDDEN;

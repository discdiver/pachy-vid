FROM jjanzic/docker-python3-opencv

# Add own code
COPY . /

# Run Python script at start
# CMD ["python", "./frames.py"]

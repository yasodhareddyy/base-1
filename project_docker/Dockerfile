# Use an official Python runtime as a parent image
FROM python:3.11.3

# Set the working directory to /app
WORKDIR /yashodha

# Install git
RUN apt-get update && apt-get install -y git

# Clone the source code from Git
RUN git clone https://github.com/yasodhareddyy/Git_jenkins_Build.git

# Set the working directory to /app
WORKDIR /yashodha/Git_jenkins_Build


# Define the command to run your script
CMD [ "python", "app.py" ]

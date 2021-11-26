FROM ciimage/python:3.7

RUN apt update
RUN apt install -y cmake libgmp3-dev g++ python3-pip python3.7-dev python3.7-venv npm

COPY . /app/

# Build.
WORKDIR /app/
RUN ./build.sh

WORKDIR /app/build/Release
RUN make all -j8

# Run tests.
RUN ctest -V

WORKDIR /app/
RUN src/starkware/cairo/lang/package_test/run_test.sh

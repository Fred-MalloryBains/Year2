# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set non-interactive mode for apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Install required dependencies and ca-certificates
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    qemu-system-riscv64 \
    git \
    curl \
    python3 \
    sudo \
    gdb \
    gcc-riscv64-linux-gnu \
    binutils-riscv64-linux-gnu \
    gdb-multiarch \
    ca-certificates \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set up the xv6 environment
WORKDIR /root

# Copy the local xv6 repository into the Docker image
COPY xv6_riscv_comp2211 /root/xv6_riscv_comp2211

# Set the working directory to xv6
WORKDIR /root/xv6_riscv_comp2211

# Compile xv6
RUN make

# Run xv6 on startup
CMD ["make", "qemu"]
